# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-17 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betting', '0041_possiblegame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='possiblegame',
            name='line',
            field=models.CharField(max_length=200),
        ),
    ]