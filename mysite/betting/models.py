from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class WeekNum(models.Model):
	week_num = models.IntegerField('Week Number', default=0)
	start_date = models.DateField('Week Starting', default=datetime.date(2017, 1, 1))
	is_current_week = models.BooleanField('Current Week?', default=False)
	def __str__(self):
		return str(self.week_num)

class Game(models.Model):
	game_text = models.CharField('Game Index', max_length=200, default='game')
	week = models.IntegerField('Week in Season', default = 0)
	home_team = models.CharField(max_length=200, default='')
	home_score = models.CharField(max_length=200, default='N/A')
	away_team = models.CharField(max_length=200, default='')
	away_score = models.CharField(max_length=200, default='N/A')
	favorite = models.CharField(max_length=200)
	line = models.FloatField(default=0)
	network = models.CharField(max_length=200)
	game_time = models.DateTimeField('game time/date', default=datetime.datetime(2017, 1, 1, 18, 00))
	game_of_week = models.BooleanField(default=False)
	def __str__(self):
		return "game"

class PossibleGame(models.Model):
	home = models.CharField(max_length=200)
	away = models.CharField(max_length=200)
	line = models.CharField(max_length=200)
	date = models.DateTimeField('game time/date', default=datetime.datetime(2017, 1, 1, 18, 00))
		
class Player(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	score = models.IntegerField('Winston Cup Points', default=0)
	last_week_score = models.IntegerField('Last Week\'s Points', default=0)
	is_paid = models.BooleanField('Paid?', default=True)
	def __str__(self):
		return self.user.username

class SavedPick(models.Model):
	id = models.AutoField(primary_key=True)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	week = models.IntegerField('Week in Season', default = 0)
	game_id = models.IntegerField('Game_ID', default=0)
	team = models.CharField('Team Name', max_length=200, default='')
	is_high_risk = models.BooleanField(default=False)
	def __str__(self):
		return 'saved pick'

class GameOfWeekScore(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	week = models.IntegerField(default=0)
	score = models.IntegerField('Game of Week Score', default=0)
	def __str__(self):
		return "Game of Week Score"
	
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
    instance.player.save()
		
