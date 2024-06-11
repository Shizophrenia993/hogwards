from django.urls import path

from src.apps.books import views

urlpatterns = [
    path("books/", views.books_view, name="book-list"),
    path('book/<int:book_id>/', views.book_detail_view, name='book_detail'),
    path('delete-book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('add-book/<int:book_id>/', views.add_book_view, name='add_book'),
    path('read-book/<int:book_id>/', views.read_book_view, name='read_book'),
]
