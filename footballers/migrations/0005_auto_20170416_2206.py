# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-16 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footballers', '0004_auto_20170416_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballplayer',
            name='birth_date',
            field=models.CharField(max_length=10),
        ),
    ]