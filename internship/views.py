from django.shortcuts import render, HttpResponse
from .models import Internship
from courses.models import Course


def main_page(request):
    internship_list = Internship.objects.all()
    context = {
        "title": "Main Page",
        "internship_list": internship_list
    }
    course_list = Course.objects.all()
    context['course_list'] = course_list
    return render(request, "internship/index.html", context)
