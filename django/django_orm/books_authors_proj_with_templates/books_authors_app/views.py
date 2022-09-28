from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *


def index(request):
    context = {
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', context)


def add_book(request):
    title = request.POST['title']
    description = request.POST['desc']
    Book.objects.create(title=title, desc=description)
    return redirect('/')


def delete_book(request):
    c = Book.objects.get(id=(request.POST['book_id']))
    c.delete()
    return redirect('/')


def author(request):
    context = {
        'authors': Author.objects.all(),
    }
    return render(request, 'author.html', context)


def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    note = request.POST['note']
    Author.objects.create(first_name=first_name,
                          last_name=last_name, notes=note)
    return redirect('/author')


def delete_book(request):
    c = Author.objects.get(id=(request.POST['author_id']))
    c.delete()
    return redirect('/author')


def book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'book_authors': Book.objects.get(id=book_id).authors.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, 'books.html', context)


def add_new_author(request, book_id):
    book = Book.objects.get(id=book_id)
    author_id = request.POST['authors']
    author = Author.objects.get(id=author_id)
    book.authors.add(author_id)
    return redirect(f'/book/{book_id}')


def author_info(request, author_id):
    context = {
        'author': Author.objects.get(id=author_id),
        'authors_info': Author.objects.get(id=author_id).books.all(),
        'all_books': Book.objects.all()
    }
    return render(request, 'author_info.html', context)


def add_new_book(request, author_id):
    author = Author.objects.get(id=author_id)
    book_id = request.POST['books']
    book = Author.objects.get(id=book_id)
    author.books.add(book_id)
    return redirect(f'/author/{author_id}')
