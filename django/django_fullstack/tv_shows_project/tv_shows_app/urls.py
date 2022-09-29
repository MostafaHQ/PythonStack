from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.show),
    path('shows/new', views.create_show),
    path('shows/create/', views.add_new_show),
    path('shows/<int:id>/', views.display_show),
]
