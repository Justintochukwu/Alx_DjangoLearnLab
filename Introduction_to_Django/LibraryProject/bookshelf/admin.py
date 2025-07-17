from django.contrib import admin
from .models import Book
class Book Admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    
admin.site.register(Book)