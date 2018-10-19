# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 22:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0010_auto_20171106_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_text',
            field=models.CharField(max_length=200, verbose_name='Game Index'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 6, 22, 17, 57, 35238, tzinfo=utc), verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='player',
            name='isActive',
            field=models.BooleanField(default=True, verbose_name='Paid?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='score',
            field=models.IntegerField(default=0, verbose_name='Winston Cup Points'),
        ),
    ]