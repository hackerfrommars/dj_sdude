from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^main/$', views.main_page),
]
