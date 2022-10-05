from django.urls import path
from . import views

urlpatterns = [
    path('', views.book),
    path('add_book', views.add_book),
    path('favorite/<int:book_id>', views.add_favorite),
    path('<int:book_id>', views.show_book),
    path('<int:book_id>/unfavorite', views.unfavorite_book),
    path('<int:book_id>/update', views.update_book),
    path('<int:book_id>/delete', views.delete_book),
    path('<int:book_id>/add_to_favorite', views.add_to_favorite)
]
