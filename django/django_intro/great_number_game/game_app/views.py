from multiprocessing import context
from django.shortcuts import render, redirect
import random


def index(request):
    if 'random' not in request.session:
        request.session['random'] = random.randint(1, 100)
    print(request.session['random'])
    return render(request, 'index.html')


def guess(request):
    if int(request.POST['number']) == request.session['random']:
        context = {
            'color': '#009E0F',
            'result': (f"{request.POST['number']} was the number!"),
        }

    elif int(request.POST['number']) > request.session['random']:
        context = {
            'color': '#CF2A27',
            'result': ("too high!"),
        }

    elif int(request.POST['number']) < request.session['random']:
        context = {
            'color': '#CF2A27',
            'result': ("too low!"),
        }

    return render(request, 'results.html', context)
