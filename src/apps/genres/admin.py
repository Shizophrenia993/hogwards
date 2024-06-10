from django.contrib import admin

from src.apps.genres.models import Genre


@admin.register(Genre)
class AuthorAdmin(admin.ModelAdmin):
	pass
