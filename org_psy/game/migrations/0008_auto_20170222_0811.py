# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_auto_20170215_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='point_calc',
        ),
        migrations.AddField(
            model_name='game',
            name='point_calc_private',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='game',
            name='point_calc_public',
            field=models.IntegerField(default=2),
        ),
    ]