# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0006_auto_20170215_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='all_doate_list',
        ),
        migrations.AddField(
            model_name='player',
            name='all_donate_list',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='player',
            name='total_donate',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]