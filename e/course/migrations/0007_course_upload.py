# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-29 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20160323_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='upload',
            field=models.FileField(default=1, upload_to='courses/'),
            preserve_default=False,
        ),
    ]