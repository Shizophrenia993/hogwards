from django.shortcuts import render

from src.apps.books.models import Book


def books_view(request):
    books = Book.objects.all()
    return render(request, 'all_cards.html', {'books': books})
