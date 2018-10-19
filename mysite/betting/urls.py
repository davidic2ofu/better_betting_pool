from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings


from . import views, admin

app_name = 'betting'
urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
	
	url(r'^logout/$', auth_views.logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

	url(r'^index/$', views.index, name='index'),
	
	url(r'^signup/$', views.signup, name='signup'),
	
	url(r'^api/$', views.api, name='api'),
	
	url(r'^scores/$', views.scores, name='scores'),
    
]