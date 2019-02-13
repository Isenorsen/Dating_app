from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('my_forms', views.my_forms, name='forms'),
    path('create_form', views.create_form, name='create_form'),
]