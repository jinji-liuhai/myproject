# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-06 22:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_renthousemeet'),
    ]

    operations = [
        migrations.AddField(
            model_name='renthousemeet',
            name='comp_meet_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 6, 22, 58, 58, 71529), verbose_name='\u5df2\u9884\u7ea6\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='renthousemeet',
            name='status',
            field=models.IntegerField(choices=[(0, '\u5f85\u9884\u7ea6'), (1, '\u5df2\u9884\u7ea6')], default=0, verbose_name='\u72b6\u6001'),
        ),
    ]
