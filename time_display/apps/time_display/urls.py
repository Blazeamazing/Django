from django.conf.urls import urls
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
]