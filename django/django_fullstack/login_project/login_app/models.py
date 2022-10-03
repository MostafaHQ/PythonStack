from django.db import models
import re


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email adress!'

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name should ba at least 2 characters'

        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name should ba at least 2 characters'

        if len(postData['password']) < 10:
            errors['password'] = 'Password should be at least 10 characters'

        if (postData['password']) != (postData['conf_pw']):
            errors['conf_pw'] = 'Your Password is wrong'

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
