# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 08:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_entity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'permissions': (('can_view', 'Can View'), ('can_modify', 'Can Modify'), ('can_create', 'Can Create'), ('can_delete', 'Can Delete'), ('can_list', 'Can See List'))},
        ),
        migrations.DeleteModel(
            name='Entity',
        ),
    ]