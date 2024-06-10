from django.contrib import admin

from src.apps.authors.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass
