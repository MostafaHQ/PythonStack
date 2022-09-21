from django.urls import path
from . import views


urlpatterns = [
    path('', views.counter),
    path('clear/', views.destroy),
]
