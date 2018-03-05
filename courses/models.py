from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exam(models.Model):

    YEAR_CHOICES = []
    SEMESTER_CHOICES = (
        ('sem1', 'semester 1'),
        ('sem2', 'semester 2')
    )

    for year in range(2015, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((year, year))

    # 1 = Midterm1; 2 = Mid2; 3 = Quiz; 4 = Assignment; 5 = Final
    exam_type = models.IntegerField(null=False)
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(Professor)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
    created_by = models.ForeignKey(User, null=False)
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=10, default='semester 1')

    def __str__(self):
        return "%s %s" %(self.course.name, self.exam_type)


class Feedback(models.Model):
    GRADES = (
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F'))
    YEAR_CHOICES = []
    SEMESTER_CHOICES = (
        ('sem1', 'semester 1'),
        ('sem2', 'semester 2')
    )

    for year in range(2015, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((year, year))

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course)
    professor = models.ForeignKey(Professor, null=True)
    created_by = models.ForeignKey(User, null=False)
    grade = models.CharField(max_length=2, choices=GRADES)
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    semester = models.CharField(choices=SEMESTER_CHOICES, max_length=10, default='semester 1')

    def __str__(self):
        return self.course.name
