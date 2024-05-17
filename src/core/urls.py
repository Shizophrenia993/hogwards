from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("src.apps.books.urls")),
    path("admin/", admin.site.urls),
    path("", include("src.apps.users.urls")),
]
