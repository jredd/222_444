# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 03:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourvideostream',
            name='chat',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='sixvideostream',
            name='chat',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
