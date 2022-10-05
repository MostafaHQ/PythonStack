from django.shortcuts import render, redirect
from .models import *
from books_app.models import Book
from login_app.models import User
from django.contrib import messages
import bcrypt

def book(request):
    context = {
        'logged_user': User.objects.get(id=request.session['id']),
        'books': Book.objects.all()
    }
    return render(request, 'book.html', context)


def add_book(request):
    title = request.POST['title']
    description = request.POST['desc']
    errors = Book.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/books')
    book = Book.objects.create(
        title=title, description=description, user=User.objects.get(id=request.session['id']))
    book.user_favorite.add(User.objects.get(id=request.session['id']))
    return redirect('/books')


def add_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['id'])
    # book.user_favorite.add(user) #the same
    user.books_favorite.add(book)
    return redirect('/books')


def show_book(request, book_id):
    context = {
        'logged_user': User.objects.get(id=request.session['id']),
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'show_book.html', context)


def unfavorite_book(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['id'])
    user.books_favorite.remove(book)
    return redirect(f'/books/{book_id}')


def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.title = request.POST['title']
    book.description = request.POST['desc']
    book.save()
    return redirect('/books')


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/books')


def add_to_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['id'])
    user.books_favorite.add(book)
    return redirect(f'/books/{book_id}')
