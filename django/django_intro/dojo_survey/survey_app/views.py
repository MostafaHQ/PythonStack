from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def show_result(request):
    name_on_template = request.POST['name']

    return render(request, 'result.html', name_on_template)
