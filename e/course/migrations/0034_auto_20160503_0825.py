# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0033_coursechapter_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursechapter',
            name='image',
        ),
        migrations.RemoveField(
            model_name='coursechapter',
            name='video',
        ),
    ]
