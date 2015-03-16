#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


PAYMENT_METHOD = (
    (1, u'Mensual'),
    (2, u'Quincenal'),
    (3, u'Pago único'),    
)

class Contract(models.Model):
	init_date = models.DateField(verbose_name=u'Fecha inicial')
	end_date = models.DateField(verbose_name=u'Fecha final')
	description = models.CharField(max_length=2000, verbose_name=u'Descripción')	
	amount = models.FloatField(verbose_name=u'valor del contrato')
	payment_method = models.IntegerField(choices=PAYMENT_METHOD, verbose_name=u'Forma de pago')
	contractor = models.ForeignKey('contractors.contractor', verbose_name=u'Contratista')
