# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-12 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.CharField(max_length=32)),
                ('id2', models.CharField(max_length=32)),
                ('id1deleted', models.IntegerField()),
                ('id2deleted', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromid', models.CharField(max_length=32)),
                ('toid', models.CharField(max_length=32)),
                ('text', models.CharField(max_length=128)),
                ('issent', models.IntegerField(null=True)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('chatlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instantmsg.ChatList')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('reply_channel', models.CharField(max_length=32)),
                ('online', models.IntegerField(null=True)),
            ],
        ),
    ]
