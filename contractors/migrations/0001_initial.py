# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identification', models.IntegerField(verbose_name='Identificaci\xf3n')),
                ('name', models.CharField(max_length=140, verbose_name='Nombre')),
                ('address', models.CharField(max_length=200, verbose_name='Direcci\xf3n')),
                ('telephone', models.CharField(max_length=10, verbose_name='Tel\xe9fono')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
