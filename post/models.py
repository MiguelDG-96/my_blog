from django.db import models
from datetime import date

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    publi_date = models.DateTimeField(default=date.today)
    rating = models.IntegerField(default=5)
    authores = models.ManyToManyField(Author, related_name='entries')

    def __str__(self):
        return self.headline
    