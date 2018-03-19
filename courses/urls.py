from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^main/$', views.main_page, name="main"),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^courses/(?P<id>[0-9]*)/$', views.list_course, name='list_course'),
    url(r'^courses/download/(?P<name>.*)/$', views.download, name='download_course'),
    url(r'^get_internship/$', views.get_internship, name='get_internship'),
    url(r'^$', views.home_page),
]
