# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('init_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=2000)),
                ('amount', models.FloatField()),
                ('payment_method', models.IntegerField(choices=[(1, 'Mensual'), (2, 'Quincenal'), (3, 'Pago \xfanico')])),
                ('contractor', models.ForeignKey(to='contractors.Contractor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
