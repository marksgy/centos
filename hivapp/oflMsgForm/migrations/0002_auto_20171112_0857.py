# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 08:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('oflMsgForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesstoken',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 12, 8, 57, 35, 519464, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='peopleformid',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 12, 8, 57, 35, 519026, tzinfo=utc)),
        ),
    ]
