from django.contrib import admin
from .models import Author, Series, Sort, Book

# Register your models here.
admin.site.register(Author)
admin.site.register(Series)
admin.site.register(Sort)
admin.site.register(Book)