# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import IntegrityError

from .models import List

def list(request, list):
	if request.user.is_authenticated():
		pass
	else:
		return render(request, 'list/login.html')

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
			return HttpResponse("asdasd")

	else:
		return render(request, 'list/login.html')

def signup(request):
	HttpResponse('as')
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
			q = List(username=username)
			q.save()
			return render(request, 'list/signup.html', {
				'error_message': "Conta criada!"
			})
		else:
			return render(request, 'list/signup.html', {
				'error_message': "Verifique a senha novamente (deve ser diferente de nula)!"
				})
	else:
		template = loader.get_template('list/signup.html')
		return HttpResponse(template.render(None, request))