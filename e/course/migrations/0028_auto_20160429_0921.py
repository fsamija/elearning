# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-29 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0027_auto_20160429_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='questionanswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='useranswer',
            name='answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionAnswer',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
