# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-04 09:15
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0035_auto_20160503_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursechapter',
            name='html',
            field=tinymce.models.HTMLField(blank=True),
        ),
    ]
