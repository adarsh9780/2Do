from django import forms
from .models import ToDoModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserChangeForm,)

class UserCreationForm(UCF):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': 'Only alphaNumeric characters are allowed in combination with @#!()*',
            'email': None,
        }