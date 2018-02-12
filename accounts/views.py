from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect, HttpResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string

from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.contrib.auth import login

from .forms import SignUpForm

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/main')
    else:
        return redirect('/')

def account_activation_sent(request):
    return HttpResponse("Confirm Your account")