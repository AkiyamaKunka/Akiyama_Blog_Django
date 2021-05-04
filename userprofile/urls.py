
from django.contrib import admin
from django.urls import path, include
from . import views
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = 'logout'),
]