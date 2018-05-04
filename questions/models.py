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


class Log(models.Model):
    EXAM = 1
    INTERNSHIP = 2
    FEEDBACK = 3
    QUESTION = 4
    LOG_CHOICES = (
        (EXAM, 1),
        (INTERNSHIP, 2),
        (FEEDBACK, 3),
        (QUESTION, 4)
    )
    log_type = models.IntegerField(choices=LOG_CHOICES, max_length=1)
    log_time = models.DateTimeField(auto_now_add=True)
    log_ref = models.IntegerField()


    def as_json(self):
        return dict(
            log_id=self.id,
            log_type=self.log_type,
            log_time=self.log_time.isoformat(),
            log_ref=self.log_ref
        )