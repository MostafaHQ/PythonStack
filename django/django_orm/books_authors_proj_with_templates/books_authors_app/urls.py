
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('delete_book', views.delete_book),
    path('add_book', views.add_book),
    path('author/', views.author),
    path('add_author', views.add_author),
    path('book/<int:book_id>', views.book),
    path('book/<int:book_id>/add_new_author', views.add_new_author),
    path('author/<int:author_id>', views.author_info),
    path('author/<int:author_id>/add_new_book', views.add_new_book),
]
