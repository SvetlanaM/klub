# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aklub', '0001_squashed_0048_auto_20171021_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userincampaign',
            name='variable_symbol',
            field=models.CharField(blank=True, default='', max_length=30, unique=True, verbose_name='Variable symbol'),
        ),
    ]