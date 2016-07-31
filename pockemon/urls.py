from django.conf.urls import url
from django.contrib import admin
from pockemon import views

urlpatterns = [
    url(r'^pockemon_list', views., name='pockemon_list'),
]