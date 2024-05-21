from django.shortcuts import render

from src.apps.books.models import Book


def books_view(request):
    books = Book.objects.all()
    return render(request, 'all_cards.html', {'books': books})


def book_detail_view(request, book_id):
    book = Book.objects.get(id=book_id)
    # author = book.author.all()[0]
    return render(request, 'book_detail.html', {'book': book})
