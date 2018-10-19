# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 05:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0018_auto_20171106_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 5, 13, 30, 604087, tzinfo=utc), verbose_name='game time/date'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 5, 13, 30, 604087, tzinfo=utc), verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='weeknum',
            name='date_start',
            field=models.DateField(default=datetime.date(2017, 11, 7), verbose_name='Week Starting'),
        ),
    ]