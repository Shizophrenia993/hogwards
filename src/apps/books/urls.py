from django.urls import path

from src.apps.books import views

urlpatterns = [
    path("books/", views.books_view, name="book-list"),
    path('book/<int:book_id>/', views.book_detail_view, name='book_detail'),
]
