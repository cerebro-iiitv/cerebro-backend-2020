from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]