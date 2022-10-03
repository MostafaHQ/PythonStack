from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('regist', views.register),
    path('success', views.welcome),
    path('login', views.login),
    path('success/logout/', views.logout),
]
