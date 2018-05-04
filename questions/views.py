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
from .forms import QuestionForm, AnswerForm

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from courses.models import Course
from .models import Question, Answer, Notification, Log


@login_required(login_url='/')
def main_page(request):
    course_list = Course.objects.all()
    question_list = Question.objects.all()
    context = {
        "course_list": course_list,
        "question_list": question_list,
        "title": "Questions Page",
        "username": request.user.username
    }
    if request.method == 'POST' and request.POST['submit'] == 'Create Question':
        question_form = QuestionForm(request.POST)
        if question_form.is_valid():
            ins = question_form.save(commit=False)
            ins.created_by = request.user
            ins.save()
            return redirect("/questions")
        else:
            return HttpResponse("not valid feedback form")
    elif request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    question_form = QuestionForm()
    form = PasswordChangeForm(request.user)
    context['password_change_form'] = form
    context['question_form'] = question_form
    return render(request, "questions/index.html", context)


@login_required(login_url='/')
def question_page(request, id):
    course_list = Course.objects.all()
    question = get_object_or_404(Question, id=id)
    answer_list = Answer.objects.filter(to_question=id)
    context = {
        "course_list": course_list,
        "question": question,
        "answer_list": answer_list,
        "title": "Questions Page",
        "username": request.user.username
    }
    if request.method == 'POST' and request.POST['submit'] == 'Create Comment':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            ins = answer_form.save(commit=False)
            ins.to_question = get_object_or_404(Question, id=id)
            ins.created_by = request.user
            ins.save()
            return redirect('/questions/question/%s' % id)
        else:
            return HttpResponse("not valid feedback form")
    elif request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    answer_form = AnswerForm()
    context['answer_form'] = answer_form
    return render(request, "questions/question.html", context)


@login_required(login_url='/')
def get_answer(request):
    question_pk = request.GET.get('question_pk', None)
    answer = get_list_or_404(Answer, to_question__pk=question_pk)
    # answer_serialized = serializers.serialize('json', answer)
    answer_json = [ob.as_json() for ob in answer]
    return HttpResponse(json.dumps(answer_json), content_type='application/json')


@login_required(login_url='/')
def notification_page(request, pk):
    notification = get_object_or_404(Notification, pk=pk, is_active=True)
    question_id = notification.question_id
    notification.is_active=False
    notification.save()
    return redirect("/questions/question/" + str(question_id.id) + "/")


@login_required(login_url='/')
def notification_list(request):
    course_list = Course.objects.all()
    question_list = Question.objects.all()
    notification_list = Notification.objects.filter(user_id=request.user, is_active=True)
    context = {
        "course_list": course_list,
        "question_list": question_list,
        "title": "Questions Page",
        "notification_list": notification_list,
        "notification_count": len(notification_list),
        "username": request.user.username
    }
    form = PasswordChangeForm(request.user)
    context['password_change_form'] = form
    return render(request, "questions/notification.html", context)


@login_required(login_url='/')
def notification_update(request):
    notifications = get_list_or_404(Notification, user_id=request.user, is_active=True)
    lng = len(notifications)
    notification_json = [ob.as_json() for ob in notifications]
    # print(notification_json)
    if lng > 0:
        return HttpResponse(json.dumps(notification_json), content_type='application/json')
    else:
        return HttpResponse('')


@login_required(login_url='/')
def delete_notification(request, id):
    notification = get_object_or_404(Notification, user_id=request.user, id=id)
    q_id = notification.question_id.id
    notification.is_active = False
    notification.save()
    return redirect("/questions/question/" + str(q_id) + "/")


@login_required(login_url='/')
def log_update(request):
    logs = Log.objects.all().order_by('-log_time')[:4]
    lng = len(logs)
    log_json = [ob.as_json() for ob in logs]
    # print(notification_json)
    if lng > 0:
        return HttpResponse(json.dumps(log_json), content_type='application/json')
    else:
        return HttpResponse('')
