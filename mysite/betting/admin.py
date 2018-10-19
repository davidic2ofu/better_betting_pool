from django.contrib import admin
from .models import Game, Player, WeekNum, SavedPick, GameOfWeekScore
from django.db import models

# work with this to get the list of games on the player admin
# class GameAdmin(admin.ModelAdmin):
	# # def get_urls(self):
		# # urls = super(GameAdmin, self).get_urls()
		# # my_urls = [
			# # url(r'^player_view/$', self.player_view),
		# # ]
		# # return my_urls + urls
		
	# def player_view(self, request):
	
		# context = ()
		
		# return TemplateResponse(request, 'admin_player.html', context)

class GameOfWeekScoreAdmin(admin.ModelAdmin):
	fields= ['player', 'week', 'score']
	list_display=['player', 'week', 'score']
	
admin.site.register(GameOfWeekScore, GameOfWeekScoreAdmin)
	
class GameAdmin(admin.ModelAdmin):
	fields = ['week', 'home_team', 'away_team', 'favorite', 'line', 'network', 'game_time', 'game_of_week']
	list_display = ('id', 'week', 'home_team', 'away_team', 'game_of_week', 'game_time')
	list_filter = ['week']
#	list_editable = ('game_time',)
	
admin.site.register(Game, GameAdmin) 

class SavedPickInline(admin.TabularInline):
	model = SavedPick
	fields = ['team', 'is_high_risk']
	extra = 0

class PlayerAdmin(admin.ModelAdmin):
	fieldsets = [
		('Player Information',	{'fields': [('user', 'is_paid'), 
											#('Player.SavedPick.team'),
											('last_week_score', 'score')]}),
		('Week\'s Picks',		{'fields': ['score']}),
	]
	inlines = [ 
		SavedPickInline, 
		]
	list_display = ('user', 'score', 'is_paid')

admin.site.register(Player, PlayerAdmin)

class WeekNumAdmin(admin.ModelAdmin):
	list_display = ('week_num', 'start_date', 'is_current_week')
	list_editable = ('is_current_week', 'start_date')

admin.site.register(WeekNum, WeekNumAdmin)

class SavedPickAdmin(admin.ModelAdmin):
	list_display = ('player', 'game_id', 'team', 'is_high_risk')
	
admin.site.register(SavedPick, SavedPickAdmin)