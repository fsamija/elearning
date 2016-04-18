# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_coursechapter_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursechapter',
            name='course_number',
        ),
        migrations.RemoveField(
            model_name='coursechapter',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='coursechapter',
            name='content',
            field=models.CharField(default='Content', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursechapter',
            name='title',
            field=models.CharField(default='Title', max_length=255),
            preserve_default=False,
        ),
    ]
