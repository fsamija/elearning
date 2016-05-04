from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Quiz(models.Model):
	name = models.CharField(max_length=255,)
	creator = models.ForeignKey(User)
	creation = models.DateField(auto_now_add=True)
	def __unicode__ (self):
		return self.name

class Question(models.Model):
	quiz = models.ForeignKey(Quiz)
	text = models.CharField(max_length=255,)

class QuestionAnswer(models.Model):
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=255,)
	is_valid = models.BooleanField()

class UserAnswer(models.Model):
	answer = models.ForeignKey(QuestionAnswer)
