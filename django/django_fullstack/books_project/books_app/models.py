from django.db import models
from login_app.models import *


class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['desc']) < 5:
            errors['first_name'] = 'Description should ba at least 5 characters'

        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='books',
                             on_delete=models.CASCADE)
    user_favorite = models.ManyToManyField(User, related_name='books_favorite')
    objects = BookManager()
