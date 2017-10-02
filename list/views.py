# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import IntegrityError
from django.urls import reverse

from .models import Board, Row

def list(request):
	if request.user.is_authenticated():
		board = Board.objects.get(username=request.user.username)
		row = board.retrieve()
		return render(request, 'list/list.html', {
			'row': row
			})
	else:
		return HttpResponseRedirect(reverse('list:login', None))

def updateRows(request):
	rows = request.POST['rows']
	i = 1
	board = Board.objects.get(username=request.user.username)
	for name in rows:
		user.sort()


def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is None:
			return render(request, 'list/login.html',{
				'error_message': "Usuário ou senha incorretos"
				})
		else:
			auth_login(request, user)
			return HttpResponseRedirect(reverse('list:list', None))

	else:
		return render(request, 'list/login.html')

def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		password_confirm = request.POST['password_confirm']
		if password == password_confirm != ('' and None):
			try:
				user = User.objects.create_user(username=username,
												email=None,
												password=password)
			except IntegrityError:
				return render(request, 'list/signup.html', {
					'error_message': "Esse usuário já existe :("
					})
			user.save()
			q = Board(username=username)
			q.save()
			auth_login(request, user)
			return HttpResponseRedirect(reverse('list:list', None))
		else:
			return render(request, 'list/signup.html', {
				'error_message': "Verifique a senha novamente (deve ser diferente de nula)!"
				})
	else:
		template = loader.get_template('list/signup.html')
		return HttpResponse(template.render(None, request))
