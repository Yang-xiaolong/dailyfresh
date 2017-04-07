# coding=utf-8
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle),
    url(r'^user_is_exist/$', views.user_is_exist),
    url(r'^login/$', views.login),
    url(r'^login_handle/$', views.login_handle),
    url(r'^user_center_info/$', views.user_center_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^logout/$', views.logout),
]