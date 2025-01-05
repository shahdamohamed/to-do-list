from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# from django.contrib.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': 'Username',
            'email': 'Email',
            'password1': 'Password',
            'passord2': 'Confirm Password',
        }