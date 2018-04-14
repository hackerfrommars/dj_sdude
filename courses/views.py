import os
from django.conf import settings
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Professor, Exam, Course, Feedback
from .forms import ExamForm, FeedbackForm
from internship.models import Internship
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, SignUpForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from questions.models import Answer, Question
from django.db.models import Count
import json
# from django.core.mail import EmailMessage
from django.core.mail import send_mail

def home_page(request):

    if request.user.is_authenticated():
        return redirect('/main')

    context = {}
    if request.method == 'POST' and request.POST['action'] == 'Login':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/main')

    elif request.method=='POST' and request.POST['action'] == 'Signup':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your SDUDE Account'
            to_email = signup_form.cleaned_data.get('email')
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # user.email_user(subject, message)
            # email = EmailMessage(subject, message, to=[to_email])
            # email.send()
            send_mail(subject, message, "sarah.hiyandao@gmail.com", [to_email], fail_silently=False)
            return redirect('/signup/account_activation_sent')
        else:
            return HttpResponse("not valid form")

    else:
        login_form = LoginForm()
        signup_form = SignUpForm()
        context['login_form'] = login_form
        context['signup_form'] = signup_form
        return render(request, "index.html", context)


@login_required(login_url='/')
def main_page(request):
    course_list = Course.objects.all()
    internship_list = Internship.objects.all().order_by('created_at')[:5][::-1]
    context = {
        "course_list": course_list,
        "title": "Main Page",
        "internship_list": internship_list
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
        form = PasswordChangeForm(request.user)
        context['password_change_form'] = form
        hot_answers = Answer.objects.values('to_question').annotate(total=Count('to_question')).order_by('-total')[:5]
        hot_questions = []
        for answer in hot_answers:
            hot_questions.append(get_object_or_404(Question, pk=answer['to_question']))
        context['hot_questions'] = hot_questions
        top_questions = Question.objects.order_by('-created_at')[:5]
        context['top_questions'] = top_questions
    return render(request, "main.html", context)


@login_required(login_url='/')
def list_course(request, id):
    exam_list = Exam.objects.filter(course=id)
    prof_list = Professor.objects.all()
    course_list = Course.objects.all()
    course = Course.objects.get(id=id)
    feedback_list = Feedback.objects.filter(course=id)
    context = {
        "exam_list": exam_list,
        "course_name": course.name,
        'prof_list': prof_list,
        "course_list": course_list,
        "feedback_list": feedback_list,  
        "course_id": id
    }
    exam_form = ExamForm()
    feedback_form = FeedbackForm()
    context['form'] = exam_form
    context['feedback_form'] = feedback_form
    if request.method == 'POST' and request.POST['submit'] == 'Create Post':
        exam_form = ExamForm(request.POST, request.FILES)
        if exam_form.is_valid():
            ins = exam_form.save(commit=False)
            ins.created_by = request.user
            ins.course = course
            ins.save()
            return redirect('/courses/%s' %id)

    elif request.method == 'POST' and request.POST['submit'] == 'Add Feedback':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            ins = feedback_form.save(commit=False)
            ins.created_by = request.user
            ins.course = course
            ins.save()
            return redirect('/courses/%s' %id)
        else:
            return HttpResponse("not valid feedback form")
    if request.method == 'POST' and request.POST['submit'] == 'Change Password':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        exam_form = ExamForm()
        feedback_form = FeedbackForm()
        form = PasswordChangeForm(request.user)
        context['password_change_form'] = form
        context['form'] = exam_form
        context['feedback_form'] = feedback_form
    return render(request, "course/index.html", context)


@login_required(login_url='/')
def download(request, name):
    file_path = os.path.join(settings.MEDIA_ROOT, name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename='+os.path.basename(file_path)
            return response
    raise Http404


@login_required(login_url='/')
def get_internship(request):
    internship_pk = request.GET.get('internship_pk', None)
    answer = get_object_or_404(Internship, pk=internship_pk)
    data = {
        'title': answer.title,
        'content': answer.content,
        'created_at': answer.created_at
    }
    return JsonResponse(data)


@login_required(login_url='/')
def hot_answer(request):
    question_pk = request.GET.get('question_pk', None)
    answers = Answer.objects.filter(to_question=question_pk)[:5]
    answer_json = [ob.as_json() for ob in answers]
    return HttpResponse(json.dumps(answer_json), content_type='application/json')


@login_required(login_url='/')
def top_answer(request):
    question_pk = request.GET.get('question_pk', None)
    answers = Answer.objects.filter(to_question=question_pk)[:5]
    answer_json = [ob.as_json() for ob in answers]
    return HttpResponse(json.dumps(answer_json), content_type='application/json')
