# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 14:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_auto_20160420_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
