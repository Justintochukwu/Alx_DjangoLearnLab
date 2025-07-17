from django.contrib import admin
from .models import Book
class Book Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    
admin.site.register(Book)