from django.shortcuts import render, render_to_response, redirect
from django.utils import timezone
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Professor, Exam, Course, Feedback
from .forms import ExamForm, FeedbackForm
from django.contrib.auth.decorators import login_required
from accounts.forms import LoginForm, SignUpForm
from django.contrib.auth import login, logout, authenticate

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site



def home_page(request):
    context = {}
    if request.method=='POST' and request.POST['action'] == 'Login':
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
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
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
    prof_list = Professor.objects.all()
    exam_list = Exam.objects.all()

    context = {
        "course_list": course_list,
        "prof_list": prof_list,
        "exam_list": exam_list,
        "title": "Main Page"
    }

    if request.method == 'POST':
        exam_form = ExamForm(request.POST, request.FILES)
        if exam_form.is_valid():
            ins = exam_form.save(commit=False)
            ins.created_by = request.user
            ins.save()
            return redirect('/')
    else:
        exam_form = ExamForm()
        context['form'] = exam_form
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
        "course_id": id,
        'prof_list': prof_list,
        "course_list": course_list,
        "feedback_list": feedback_list,
    }

    if request.method == 'POST' and request.POST['submit'] == 'Create Post':
        exam_form = ExamForm(request.POST, request.FILES)
        if exam_form.is_valid():
            ins = exam_form.save(commit=False)
            ins.created_by = request.user
            ins.course = course
            ins.save()
            return HttpResponseRedirect('/courses/%s' %id)
    

    elif request.method == 'POST' and request.POST['submit'] == 'Add Feedback':
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            ins = feedback_form.save(commit=False)
            ins.created_by = request.user
            ins.course = course
            ins.save()
            return HttpResponseRedirect('/courses/%s' %id)
    else:
        exam_form = ExamForm()
        feedback_form = FeedbackForm()
        context['form'] = exam_form
        context['feedback_form'] = feedback_form
    return render(request, "course/index.html", context)
