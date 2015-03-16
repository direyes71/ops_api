#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


def home(request):
	error = ''
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				# Redirect to a success page.
				login(request, user)				
				return HttpResponseRedirect(reverse('contractor_list'))
			else:
				# Return a 'disabled account' error message
				error = 'Usuario inactivo'
		else:
			# Return an 'invalid login' error message.
			error = 'Datos invalidos'
	return render(request, 'app/home.html', {'error': error})


def logout_view(request):	
	logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect(reverse('home'))