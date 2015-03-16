#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Contractor(models.Model):	
	identification = models.IntegerField(verbose_name=u'Identificación')
	name = models.CharField(max_length=140, verbose_name=u'Nombre')
	address = models.CharField(max_length=200, verbose_name=u'Dirección')
	telephone = models.CharField(max_length=10, verbose_name=u'Teléfono')

	def __unicode__(self):
		return '{0} - {1}'.format(self.identification, self.name)