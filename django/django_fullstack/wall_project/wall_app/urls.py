from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall),
    path('message', views.post_message),
    path('comment', views.post_comment),
    path('delete', views.delete),
]
