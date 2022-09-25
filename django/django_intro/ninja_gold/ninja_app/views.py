from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'index.html')


def find_gold(request):
