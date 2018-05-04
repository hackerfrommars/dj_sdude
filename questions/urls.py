from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^question/(?P<id>.*)/$', views.question_page, name='question'),
    url(r'^notifications/$', views.notification_list, name='notification_list'),
    url(r'^notification/delete/(?P<id>.*)/$', views.delete_notification, name='delete_notification'),
    url(r'^notification/(?P<pk>.*)/$', views.notification_page, name='notification'),
    url(r'^notification_update/$', views.notification_update, name='notification_update'),
    url(r'^log_update/$', views.log_update, name='log_update'),
    url(r'^$', views.main_page, name="main"),
    url(r'^get_answer/$', views.get_answer, name="get_answer"),
]
