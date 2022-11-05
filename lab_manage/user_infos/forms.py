# app/forms.py

from django import forms
from .models import User


class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('userid', 'password')


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
