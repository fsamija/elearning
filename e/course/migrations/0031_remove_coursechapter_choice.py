# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 12:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0030_auto_20160502_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursechapter',
            name='choice',
        ),
    ]
