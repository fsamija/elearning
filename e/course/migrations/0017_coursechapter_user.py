# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 11:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0016_auto_20160414_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursechapter',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]