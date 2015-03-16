#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from contracts.forms import ContractForm
from contracts.models import Contract

# Create your views here.


@login_required
def add_contract(request):
	u""" Funtion to add a new contract
	"""
	if request.method == 'POST':
		form = ContractForm(request.POST)
		if form.is_valid():			
			contractor = form.save()
			return HttpResponseRedirect(reverse('contractor_list'))
	else:
		form = ContractForm()
	return render(request, 'contracts/add_contract.html', {'form': form})


@login_required
def contract_list(request):
	u""" Funtion to show contracts
	"""
	contracts = Contract.objects.all()	
	return render(request, 'contracts/contracts.html', {'contracts': contracts})