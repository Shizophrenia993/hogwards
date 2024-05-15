from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    birthday = models.DateField()
    description = models.TextField(null=True)

    def __str__(self):
        return self.name
