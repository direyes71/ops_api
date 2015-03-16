#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from contracts.models import Contract


class ContractForm(ModelForm):

	def __init__(self, *args, **kwargs):		
		super(ContractForm, self).__init__(*args, **kwargs)
		self.fields['description'] = forms.CharField(widget=forms.Textarea, max_length=2000)

	class Meta:
		model = Contract
