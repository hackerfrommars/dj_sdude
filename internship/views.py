from django.shortcuts import render, HttpResponse
from .models import Internship


def main_page(request):
    internship_list = Internship.objects.all()
    context = {
        "title": "Main Page",
        "internship_list": internship_list
    }
    return render(request, "internship/index.html", context)
