# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-29 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0019_auto_20160206_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='variable_symbol',
            field=models.CharField(default='', max_length=30, unique=True, verbose_name='Variable symbol'),
        ),
    ]
