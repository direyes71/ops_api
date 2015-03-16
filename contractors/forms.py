#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from contractors.models import Contractor


class ContractorForm(ModelForm):
	class Meta:
		model = Contractor
