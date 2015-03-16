#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from contractors.forms import ContractorForm
from contractors.models import Contractor

# Create your views here.


@login_required
def add_contractor(request):
	u""" Funtion to add a new contractor
	"""
	if request.method == 'POST':
		form = ContractorForm(request.POST)
		if form.is_valid():			
			contractor = form.save()
			return HttpResponseRedirect(reverse('contractor_list'))
	else:
		form = ContractorForm()
	return render(request, 'contractors/add_contractor.html', {'form': form})


@login_required
def contractor_list(request):
	u""" Funtion to add a new contractor
	"""
	contractors = Contractor.objects.all()
	return render(request, 'contractors/contractors.html', {'contractors': contractors})


@login_required
def contractor_edit(request, contractor_id):	
	contractor = get_object_or_404(Contractor, pk=contractor_id)	
	if request.method == 'POST':
		form = ContractorForm(request.POST, instance=contractor)
		if form.is_valid():
			contractor = form.save()
			return HttpResponseRedirect(reverse('contractor_list'))
	else:
		form = ContractorForm(instance=contractor)
	return render(request, 'contractors/add_contractor.html', {'form': form})
