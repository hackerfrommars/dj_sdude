from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.main_page, name="main"),
    url(r'^get_answer/$', views.get_answer, name="get_answer"),
]
