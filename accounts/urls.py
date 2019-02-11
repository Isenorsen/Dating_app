from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('<int:user_id>', views.user_account, name='user'),
    path('profile', views.my_profile, name='profile'),
    path('messages', views.user_mail, name='messages'),
    path('logout', views.logout, name='logout')
]