# relationship_app/forms.py

from django import forms
from .models import Book  # or your actual model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
