# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-12 03:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0035_auto_20171111_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedpick',
            name='game_id',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False, verbose_name='Game_ID'),
        ),
    ]