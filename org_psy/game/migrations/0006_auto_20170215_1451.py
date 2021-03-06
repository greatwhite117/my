# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20170202_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='punish_bool',
            new_name='feedback_my_donate_public',
        ),
        migrations.RemoveField(
            model_name='game',
            name='conditional_type',
        ),
        migrations.RemoveField(
            model_name='game',
            name='feedback_contents',
        ),
        migrations.RemoveField(
            model_name='game',
            name='feedback_show',
        ),
        migrations.RemoveField(
            model_name='game',
            name='feedback_type',
        ),
        migrations.RemoveField(
            model_name='game',
            name='range_down',
        ),
        migrations.RemoveField(
            model_name='game',
            name='range_up',
        ),
        migrations.RemoveField(
            model_name='game',
            name='reward',
        ),
        migrations.AddField(
            model_name='game',
            name='feedback_my_only',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='feedback_my_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='feedback_my_total',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='feedback_other_donate_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='game',
            name='reward_On_Off',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='all_doate_list',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='wait_time',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='total_donate',
            field=models.CharField(default='', max_length=10, null=True),
        ),
    ]
