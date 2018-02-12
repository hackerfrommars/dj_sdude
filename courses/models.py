from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exam(models.Model):

    # 1 = Midterm1; 2 = Mid2; 3 = Quiz; 4 = Assignment; 5 = Final
    exam_type = models.IntegerField(null=False)
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(Professor)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
    created_by = models.ForeignKey(User, null=False)

    def __str__(self):
        return "%s %s" %(self.course.name, self.exam_type)


class Feedback(models.Model):
    # grades = {
    #     "A" : 1,
    #     "A-" : 2,
    #     ""
    # }
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(Professor, null=True)
    created_by = models.ForeignKey(User, null=False)
    # grade = "A" "A-" "B" "B+ etc"

    def __str__(self):
        return self.course.name