from django.conf.urls import url

from . import views

app_name = 'list'
urlpatterns = [
	url(r'^$', views.login, name='login'),
	url(r'register/$', views.signup, name='signup'),
	url(r'list/$', views.list, name='list'),
	url(r'updateRows/$', views.updateRows, name='updateRows'),
	url(r'createRow/$', views.createRow, name='createRow'),
	url(r'updateLists/$', views.updateLists, name='updateLists'),
	url(r'deleteItem/$', views.deleteItem, name='deleteItem'),
	url(r'compareItem/$', views.compareItem, name='compareItem')
]