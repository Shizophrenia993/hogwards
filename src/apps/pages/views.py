from django.shortcuts import render
from django.views.generic import TemplateView

from src.apps.books.models import Book


def page_not_found_view(request, exception):
    return render(request, "pages/404.html")


def recomendation_book_view(request):
    all_books = Book.objects.order_by('?')[:4]
    return render(request, 'index.html', {'books': all_books})


class IndexView(TemplateView):
    template_name = "index.html"


class AboutView(TemplateView):
    template_name = "about.html"
