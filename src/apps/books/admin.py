from django.contrib import admin

from src.apps.books.models import Book


@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    pass
