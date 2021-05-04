"""django_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'article'
urlpatterns = [
    path('article_list/', views.show_list, name='article_list'),
    path('article_detail/<int:id>/', views.show_detail, name='article_detail'),
    path('article_submit/', views.article_submit, name='article_submit'),
    path('article_delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article_update/<int:id>/', views.article_update, name='article_update'),
]