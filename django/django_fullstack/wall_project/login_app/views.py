from contextlib import redirect_stderr
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    user = User.objects.create(first_name=first_name,
                               last_name=last_name, email=email, password=pw_hash)
    print(pw_hash)
    request.session['id'] = user.id
    return redirect('/success')


def welcome(request):
    try:
        if request.session['id']:
            context = {
                'user': User.objects.get(id=request.session['id'])
            }
        return redirect('/wall/')
    except:
        return redirect('/')


def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['id'] = logged_user.id
            return redirect('/success')
    return redirect('/')


def logout(request):
    del request.session['id']
    return redirect('/')
