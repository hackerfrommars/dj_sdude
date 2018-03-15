from django.shortcuts import render, HttpResponse, redirect
from .models import Internship
from courses.models import Course
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash


def main_page(request):
    if request.method == 'POST' and request.POST['submit'] == 'Change Password':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    internship_list = Internship.objects.all()
    context = {
        "title": "Main Page",
        "internship_list": internship_list
    }
    course_list = Course.objects.all()
    context['course_list'] = course_list
    form = PasswordChangeForm(request.user)
    context['password_change_form'] = form
    return render(request, "internship/index.html", context)
