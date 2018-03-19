import os
from django.conf import settings
from django.shortcuts import render, render_to_response, redirect, get_object_or_404, get_list_or_404
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, SignUpForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
import json
from django.core.serializers.json import DjangoJSONEncoder

from courses.models import Course
from .models import Question, Answer

@login_required(login_url='/')
def main_page(request):
    course_list = Course.objects.all()
    question_list = Question.objects.all()
    context = {
        "course_list": course_list,
        "question_list": question_list,
        "title": "Questions Page",
    }
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        for question in question_list:
            context[str(question.pk)] = Answer.objects.filter(to_question=question.pk)
        form = PasswordChangeForm(request.user)
        context['password_change_form'] = form
    return render(request, "questions/index.html", context)


def get_answer(request):
    question_pk = request.GET.get('question_pk', None)
    answer = get_list_or_404(Answer, to_question__pk=question_pk)
    data = {
        'answer': len(answer)
    }
    return JsonResponse(data)
