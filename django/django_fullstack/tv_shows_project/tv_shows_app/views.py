from django.shortcuts import render, redirect
from .models import *


def show(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(request, 'shows.html', context)


def index(request):
    return redirect('/shows')


def create_show(request):
    return render(request, 'add_show.html')


def add_new_show(request):
    title = request.POST['title']
    network = request.POST['network']
    release_date = request.POST['release_date']
    c = Show.objects.create(title=title, network=network,
                            release_date=release_date)
    return redirect(f'/shows/{c.id}/')


def display_show(request, id):
    context = {
        'show': Show.objects.get(id=id),
    }
    return render(request, 'show_page.html', context)
