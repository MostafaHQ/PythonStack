from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('earn', views.find_gold)
]
