from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Series(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

class Sort(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    sort = models.ForeignKey(Sort, on_delete=models.CASCADE)
    short_description = models.TextField(default='lorem ipsum')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self) -> str:
        return self.title