import re
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


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
    description = request.POST['desc']
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect("/shows/new")
    c = Show.objects.create(title=title, network=network,
                            release_date=release_date, desc=description)
    return redirect(f'/shows/{c.id}/')


def display_show(request, id):
    context = {
        'show': Show.objects.get(id=id),
    }
    return render(request, 'show_page.html', context)


def back(request):
    return redirect('/shows')


def edit_show(request, id):
    show = Show.objects.get(id=id)
    show.release_date = show.release_date.strftime('%Y-%m-%d')
    context = {
        'show': show
    }
    return render(request, 'edit_page.html', context)


def update_show(request, id):
    c = Show.objects.get(id=id)
    c.title = request.POST['title']
    c.network = request.POST['network']
    c.release_date = request.POST['release_date']
    c.desc = request.POST['desc']
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect(f'/shows/{c.id}/edit')
    c.save()

    return redirect(f'/shows/{c.id}/')


def go_to_show(request, id):
    return redirect(f'/shows/{id}/')


def delete(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/')


def delete_from_table(request, id):
    Show.objects.get(id=id).delete()
    return redirect('/')


def edit_from_table(request, id):
    return redirect(f'/shows/{id}/edit')


def show_from_table(request, id):
    return redirect(f'/shows/{id}')
