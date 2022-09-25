from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_details),
    path('add_user', views.adding_user),
    path('delete_user', views.delete_user),
]
