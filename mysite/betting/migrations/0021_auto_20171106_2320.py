# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 05:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0020_auto_20171106_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 5, 20, 12, 133226, tzinfo=utc), verbose_name='game time/date'),
        ),
        migrations.AlterField(
            model_name='game',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 7, 5, 20, 12, 133226, tzinfo=utc), verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='game',
            name='week',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='betting.WeekNum'),
        ),
    ]
