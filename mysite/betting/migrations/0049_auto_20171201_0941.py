# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0048_auto_20171201_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedpick',
            name='game_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Game_ID'),
        ),
    ]
