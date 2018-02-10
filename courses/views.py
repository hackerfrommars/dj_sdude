from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.http import Http404, HttpResponse
from .models import Professor, Exam, Course


def home_page(request):

    return render(request, "index.html", context= {})

def main_page(request):
    course_list = Course.objects.all()
    prof_list = Professor.objects.all()
    exam_list = Exam.objects.all()

    context = {
        "course_list": course_list,
        "prof_list": prof_list,
        "exam_list": exam_list,
        "title": "Main Page"
    }
    #testing purpose for bot

    return render(request, "main.html", context)