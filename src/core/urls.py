from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from src.apps.pages import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.recomendation_book_view, name="home"),
    path("", include("src.apps.books.urls")),
    path("", include("src.apps.users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
