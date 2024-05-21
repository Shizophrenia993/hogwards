from django.urls import path

from src.apps.books import views

urlpatterns = [
    path("", views.books_view, name="main"),
    path('book/<int:book_id>/', views.book_detail_view, name='book_detail'),
]
