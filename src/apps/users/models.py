from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    birthday = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=255, default="Гость")
    book_reservations = models.ManyToManyField(
        "books.Book", related_name="reservations"
    )
