from django.test import TestCase
from django.contrib.auth.models import User
from .models import Player

class PlayerModelTests(TestCase):
	def test_first_name(self):
		u = User(username='test', password='test')
		u.save()
		p = Player(user=u)
		self.assertIs(p.user.username, True)