from django.db import models
from django.contrib.auth.models import User
import datetime


class Question(models.Model):
    created_by = models.ForeignKey(User, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.content


class Answer(models.Model):
    to_question = models.ForeignKey(Question, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=False)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.content

    def as_json(self):
        return dict(
            created_at=self.created_at.isoformat(),
            content=self.content,
            question_pk=self.to_question.pk
        )


class Notification(models.Model):
    question_id = models.ForeignKey(Question, null=False)
    is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, null=False)


    def as_json(self):
        return dict(
            notification_id=self.id,
            id=self.question_id.pk,
            question=self.question_id.content
        )