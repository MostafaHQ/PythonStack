from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('regist', views.register),
    path('success', views.welcome),
    path('login', views.login),
    path('wall/logout/', views.logout),
]
