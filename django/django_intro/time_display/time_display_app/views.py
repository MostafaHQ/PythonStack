from django.shortcuts import render
from time import strftime


def timeDisplay(request):
    context = {
        "time": strftime("%Y-%m %H:%M %p")
    }
    return render(request, 'index.html', context)
