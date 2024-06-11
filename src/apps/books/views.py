from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from src.apps.books.models import Book


def books_view(request):
    books = Book.objects.all()
    return render(request, 'all_cards.html', {'books': books})


def book_detail_view(request, book_id):
    book = Book.objects.prefetch_related('author', 'genre').get(id=book_id)
    print(book.author.all())
    return render(request, 'book_detail.html', {'book': book, "genres": book.genre.all(), "authors": book.author.all()})


@login_required(login_url=reverse_lazy("login"))
def delete_book(request, book_id):
    user = request.user
    book = Book.objects.get(id=book_id)
    user.book_reservations.remove(book)
    return redirect("profile")


@login_required(login_url=reverse_lazy("login"))
def add_book_view(request, book_id):
    user = request.user
    book = Book.objects.get(id=book_id)
    user.book_reservations.add(book)
    return redirect("profile")


@login_required(login_url=reverse_lazy("login"))
def read_book_view(request, book_id):
    user = request.user
    user.count_read_books += 1
    user.save()
    book = Book.objects.get(id=book_id)
    user.book_reservations.remove(book)
    return redirect("profile")
