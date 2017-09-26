from django.conf.urls import url

from . import views

app_name = 'list'
urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'register/$', views.signup, name='signup'),
	url(r'list/$', views.list, name='list')
]