from django.shortcuts import render, HttpResponse


def main_page(request):
    return HttpResponse("this page is for internships")
