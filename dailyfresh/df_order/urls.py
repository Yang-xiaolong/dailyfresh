# coding=utf-8
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.order),
    url(r'^submit/$', views.order_submit),
    url(r'^pay/$', views.order_pay),
]

