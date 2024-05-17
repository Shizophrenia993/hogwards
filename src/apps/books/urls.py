from django.urls import path

from src.apps.books.views import books_view

urlpatterns = [
    path("", books_view, name="main"),
]
