# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='kind',
            field=models.CharField(choices=[('A', 'Individual'), ('B', 'Individual_plus'), ('C', 'Station'), ('D', 'Station_plus'), ('E', 'orgnization')], max_length=1, verbose_name='\u7528\u6237\u7c7b\u578b'),
        ),
    ]
