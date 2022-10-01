from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.show),
    path('shows/new', views.create_show),
    path('shows/create/', views.add_new_show),
    path('shows/<int:id>/', views.display_show),
    path('shows/', views.back),
    path('shows/<int:id>/edit/', views.edit_show),
    path('shows/<int:id>/update', views.update_show),
    path('shows/create/', views.go_to_show),
    path('shows/<int:id>/destroy/', views.delete),
    path('shows/<int:id>/edit/', views.edit_from_table),
    path('shows/<int:id>/', views.show_from_table),
    path('shows/destroy/', views.delete_from_table),
]
