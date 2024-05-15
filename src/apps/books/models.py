from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.IntegerField()
    count = models.IntegerField(default=1)
    author = models.ManyToManyField("authors.Author")
    genre = models.ManyToManyField("genres.Genre")
