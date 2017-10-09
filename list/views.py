# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from django.db import IntegrityError
from django.urls import reverse

from .models import Board, Row, Item

def compareItem(request):
	if request.user.is_authenticated() and request.method == 'POST':
		board = Board.objects.get(username=request.user.username)
		text = request.POST['text']
		rows = board.row_set.all()
		exist = False
		for row in rows:
			exist = row.item_set.filter(text__iexact=text).exists()
			if exist:
				break
		data = {'exist': exist}
		return JsonResponse(data)
	return HttpResponseRedirect(reverse('list:login', None))

def deleteItem(request):
	if request.user.is_authenticated() and request.method == 'POST':
		board = Board.objects.get(username=request.user.username)
		row = request.POST['row']
		row = board.row_set.get(name=row)
		item = request.POST['item']
		item = row.item_set.get(text=item)
		row.remove(item, True)
		return JsonResponse(None, safe=False)
	return HttpResponseRedirect(reverse('list:login', None))

def updateLists(request):
	if request.user.is_authenticated() and request.method == 'POST':
		board = Board.objects.get(username=request.user.username)
		dest_row = request.POST['dest_row']
		dest_row = board.row_set.get(name=dest_row)
		item_names = request.POST.getlist('item_names[]')
		i = 0
		print item_names
		for name in item_names:
			try:
				item = dest_row.item_set.get(text=name)
				dest_row.sort(item, i, False)
			except Item.DoesNotExist:
				item = dest_row.item_set.create(text=name)
				dest_row.sort(item, i, True)
			i+=1
		items = dest_row.retrieve()
		return JsonResponse(None, safe=False)
	return HttpResponseRedirect(reverse('list:login', None))

def updateRows(request):
	if request.user.is_authenticated() and request.method == 'POST':
		row_names = request.POST.getlist('row_names[]')
		board = Board.objects.get(username=request.user.username)
		rows = board.retrieve()
		for row in rows:
			board.remove(row, False)
		i = 0
		for name in row_names:
			row = board.row_set.get(name=name)
			board.sort(row, i, True)
			i+=1
		return JsonResponse(None, safe=False)
	return HttpResponseRedirect(reverse('list:login', None))

def createRow(request):
	if request.user.is_authenticated() and request.method == 'POST':
		name = request.POST['name']
		board = Board.objects.get(username=request.user.username)
		exist = board.row_set.filter(name__iexact=name).exists()
		if not exist:
			r = board.row_set.create(name=name)
			board.sort(r, board.size, True)
		data = {'exist': exist}
		return JsonResponse(data)
	return HttpResponseRedirect(reverse('list:login', None))

def list(request):
	if request.user.is_authenticated():
		board = Board.objects.get(username=request.user.username)
		rows = board.retrieve()
		containers = []
		class Container():
			def __init__(self, row, items):
				self.row = row
				self.items = items
		for row in rows:
			items = row.retrieve()
			c = Container(row, items)
			containers.append(c)
		return render(request, 'list/list.html', {
			'containers': containers
			})
	else:
		return HttpResponseRedirect(reverse('list:login', None))

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
