#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Login
    url(r'^$', 'app.views.home', name='home'),
    url(r'^accounts/login/$', 'app.views.home', name='home'),
    url(r'^salir$', 'app.views.logout_view', name='logout'),

    # Contractors
    url(r'^nuevo-contratista$', 'contractors.views.add_contractor', name='add_contractor'),
    url(r'^listado-contratistas$', 'contractors.views.contractor_list', name='contractor_list'),
    url(r'^editar-contratista/(?P<contractor_id>\d+)$', 'contractors.views.contractor_edit', name='contractor_edit'),

    # Contracts
    url(r'^nuevo-contrato$', 'contracts.views.add_contract', name='add_contract'),
    url(r'^listado-contratos$', 'contracts.views.contract_list', name='contract_list'),
    #url(r'^editar-contratista/(?P<contractor_id>\d+)$', 'contractors.views.contractor_edit', name='contractor_edit'),

    url(r'^admin/', include(admin.site.urls)),
)
