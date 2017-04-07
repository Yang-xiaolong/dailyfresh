from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add_goods/$', views.add_goods),
    url(r'^change/$', views.change),
    url(r'^del/$', views.cart_del),
]
