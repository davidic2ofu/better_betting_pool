# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 00:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0028_auto_20171109_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 0, 5, 44, 402416, tzinfo=utc), verbose_name='game time/date'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 10, 0, 5, 44, 402416, tzinfo=utc), verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='weeknum',
            name='start_date',
            field=models.DateField(default=datetime.date(2017, 11, 10), verbose_name='Week Starting'),
        ),
    ]