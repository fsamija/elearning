# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20160322_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'permissions': (('add_course', 'Add course'),)},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={},
        ),
    ]
