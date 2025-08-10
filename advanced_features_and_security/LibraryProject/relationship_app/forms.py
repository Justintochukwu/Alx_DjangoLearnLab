from django import forms
from django.contrib.auth.forms import UserCreationForm
from bookshelf.models import CustomUser
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'role', 'password1', 'password2')
