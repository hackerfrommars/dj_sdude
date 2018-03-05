from django.db import models
from django.contrib.auth.models import User


class Internship(models.Model):
    created_by = models.ForeignKey(User, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(max_length=500)
    finish_time = models.DateTimeField(blank=True)

