from django.shortcuts import render, render_to_response
from django.utils import timezone
from django.http import Http404, HttpResponse

def main_page(request):

    return render(request, "main.html", context= {})