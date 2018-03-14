from django.db import models
from django.contrib.auth.models import User
import datetime


class Question(models.Model):
    created_by = models.ForeignKey(User, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)


class Answer(models.Model):
    to_question = models.ForeignKey(Question, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=False)
    content = models.TextField(max_length=500)
