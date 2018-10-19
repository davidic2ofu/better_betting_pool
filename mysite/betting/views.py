from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
import datetime, requests
from betting.forms import SignUpForm

from .models import Game, WeekNum, Player, SavedPick, GameOfWeekScore, PossibleGame


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			return redirect('login')
	else:
		return redirect('login')
		
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.save()
			#username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(request, username=user.username, password=raw_password)
			auth_login(request, user)
			return redirect('/betting/index')

	else:
		form = SignUpForm()
	return render(request, 'betting/signup.html', {'form': form})
	
def index(request):
	current_week = WeekNum.objects.get(is_current_week=True)
	q = Game.objects.filter(game_of_week=True, week=current_week.week_num)
	if len(q) > 0:
		game_of_week = Game.objects.get(game_of_week=True, week=current_week.week_num)
	else:
		game_of_week = {}
	if request.method == 'POST':
		picks = request.POST
		high_risk_game_number = 0
		for game in picks:
			if game == "high_risk":
				high_risk_game_number = int(picks[game])
			if game == "game_of_week_score":
				print("trying to save game of week score...")
				q = GameOfWeekScore.objects.filter(week=current_week.week_num, player=request.user.player)
				q.delete()
				q = GameOfWeekScore(player=request.user.player, week=current_week.week_num, score=int(picks[game]))
				q.save()
				
		for i, game in enumerate(picks):
			if i != 0 and game != "high_risk" and game != "game_of_week_score":
				if high_risk_game_number != 0 and int(game) == high_risk_game_number:
					newpick = SavedPick(player=request.user.player, game_id=int(game), team=picks[game], is_high_risk=True, week=current_week.week_num)
				else:
					newpick = SavedPick(player=request.user.player, game_id=int(game), team=picks[game], week=current_week.week_num)
				q = SavedPick.objects.filter(game_id=int(game)).filter(player=request.user.player)
				if len(q) != 0:
					q.delete()
				newpick.save()
	game_list = Game.objects.filter(week=current_week.week_num)
	player_list = Player.objects.order_by('-score')
	saved_picks = SavedPick.objects.all().filter(player=request.user.player)
	context = {'game_list': game_list, 'current_week': current_week, 'player_list': player_list,  'saved_picks': saved_picks, 'game_of_week': game_of_week}
	return render(request, 'betting/index.html', context)
	
def scores(request):
	global u
	api = "https://cfb-scoreboard-api.herokuapp.com/v1/date/"
	week_list = {
			'8':  ['20171015', '20171016', '20171017', '20171018', '20171019', '20171020', '20171021'],
			'9':  ['20171022', '20171023', '20171024', '20171025', '20171026', '20171027', '20171028'],
			'10': ['20171029', '20171030', '20171031', '20171101', '20171102', '20171103', '20171104'],
			'11': ['20171105', '20171106', '20171107', '20171108', '20171109', '20171110', '20171111'],
			'12': ['20171112', '20171113', '20171114', '20171115', '20171116', '20171117', '20171118'],
			'13': ['20171119', '20171120', '20171121', '20171122', '20171123', '20171124', '20171125'],
			'14': ['20171126', '20171127', '20171128', '20171129', '20171130', '20171201', '20171202'],
			'15': ['20171203', '20171204', '20171205', '20171206', '20171207', '20171208', '20171209']
			}
	game_list = []
	pick_list = []	
	week, week_starting, current_user, gow_score = None, None, None, None
	if request.method == 'POST':
		input = request.POST
		if 'user_choice' in input:
			current_user = input['user_choice']
			players = Player.objects.all()
			for player in players:
				if player.user.username == current_user:
					u = player
			week = input['week_choice']
			week_starting = week_list[week][0]
			week_starting = week_starting[4:6] + '/' + week_starting[6:8] + '/' + week_starting[0:4]
		
			for date in week_list[week]:
				data = requests.get(api+date).json()
				for i in range(len(data['games'])):
					home = data['games'][i]['homeTeam']['displayName']
					try:
						game = Game.objects.get(home_team=home, week=int(week))
					except Game.DoesNotExist:
						game = None
					if game is not None:
						game.home_score = data['games'][i]['scores']['home']
						game.away_score = data['games'][i]['scores']['away']
						game.save()

			game_list = Game.objects.filter(week=int(week))
			pick_list = SavedPick.objects.filter(week=int(week), player=u)
			try:
				gow_score = GameOfWeekScore.objects.get(player=u, week=int(week))
			except GameOfWeekScore.DoesNotExist:
				gow_score = None
			
		if 'points' in input:
			p = int(input['points'])
			u.score += p
			u.last_week_score = p
			u.save()

	user_list = Player.objects.all()
	context = {'user_list': user_list, 'game_list': game_list, 'pick_list': pick_list, 'week': week, 'week_starting': week_starting, 'current_user': current_user, 'gow_score': gow_score}
	return render(request, 'betting/scores.html', context)
	
def api(request):
	global global_week
	api = "https://cfb-scoreboard-api.herokuapp.com/v1/date/"
	week_list = {
			'8':  ['20171015', '20171016', '20171017', '20171018', '20171019', '20171020', '20171021'],
			'9':  ['20171022', '20171023', '20171024', '20171025', '20171026', '20171027', '20171028'],
			'10': ['20171029', '20171030', '20171031', '20171101', '20171102', '20171103', '20171104'],
			'11': ['20171105', '20171106', '20171107', '20171108', '20171109', '20171110', '20171111'],
			'12': ['20171112', '20171113', '20171114', '20171115', '20171116', '20171117', '20171118'],
			'13': ['20171119', '20171120', '20171121', '20171122', '20171123', '20171124', '20171125'],
			'14': ['20171126', '20171127', '20171128', '20171129', '20171130', '20171201', '20171202'],
			'15': ['20171203', '20171204', '20171205', '20171206', '20171207', '20171208', '20171209']
			}
	
	if request.method == 'POST':
		input = request.POST
		if 'week_choice' in input:
			PossibleGame.objects.all().delete()
			week = input['week_choice']
			global_week = int(week)
			week_starting = week_list[week][0]
			week_starting = week_starting[4:6] + '/' + week_starting[6:8] + '/' + week_starting[0:4]
			for date in week_list[week]:
				data = requests.get(api+date).json()
				for i in range(len(data['games'])):
					home = data['games'][i]['homeTeam']['displayName']
					away = data['games'][i]['awayTeam']['displayName']
					line = data['games'][i]['odds']['spread']
					date = data['games'][i]['date']
					y = int(date[0:4])
					m = int(date[5:7])
					d = int(date[8:10])
					h = int(date[11:13])
					mm = int(date[14:16])
					date = datetime.datetime(y, m, d, h, mm)
					PossibleGame.objects.create(home=home, away=away, line=line, date=date)
			game_list = PossibleGame.objects.all()
			context = {'game_list': game_list, 'week': week, 'week_starting': week_starting }
			return render(request, 'betting/api.html', context)
		if 'game_choice' in input:
			q = Game.objects.filter(week=global_week)
			q.delete()
			game_of_week = input['game_of_week']
			game_choices = input.getlist("game_choice")
			for game in game_choices:
				print(game)
			for game in game_choices:
				is_game_of_week = False
				if game.startswith('manual'):
					id = game[6:len(game)]
					homeid = 'home' + id
					awayid = 'away' + id
					lineid = 'line' + id
					networkid = 'network' + id
					dateid = 'date' + id
					if game_of_week == 'gow' + id:
						is_game_of_week = True
					home = input[homeid]
					away = input[awayid]
					line = float(input[lineid])
					network = input[networkid]
					date = input[dateid]
					y = int(date[0:4])
					m = int(date[5:7])
					d = int(date[8:10])
					h = int(date[11:13])
					mm = int(date[14:16])
					date = datetime.datetime(y, m, d, h, mm)
					if line > 0:
						favorite = home
					else:
						favorite = away
					Game.objects.create(week=global_week, home_team=home, away_team=away, favorite=favorite, line=line, network=network, game_time=date, game_of_week=is_game_of_week)
				else:
					possible = PossibleGame.objects.get(id=int(game))
					lineid = game + "_line"
					networkid = game + "_network"
					home = possible.home
					away = possible.away
					line = float(input[lineid])
					network = input[networkid]
					if line > 0:
						favorite = home
					else:
						favorite = away
					date = possible.date
					if game_of_week == game:
						is_game_of_week = True
					Game.objects.create(week=global_week, home_team=home, away_team=away, favorite=favorite, line=line, network=network, game_time=date, game_of_week=is_game_of_week)					
	context = {}
	return render(request, 'betting/api.html', context)