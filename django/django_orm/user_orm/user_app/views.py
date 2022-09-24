from multiprocessing import context
from django.shortcuts import render, redirect
from .models import User


def user_details(request):
    context = {
        "my_users": User.objects.all()
    }

    return render(request, 'index.html', context)

def adding_user(request):
    return redirect()