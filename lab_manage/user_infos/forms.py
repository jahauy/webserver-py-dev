# app/forms.py

from django import forms
from .models import User
from captcha.fields import CaptchaField


class UserLoginForm(forms.Form):
    userid = forms.CharField(label="用户id", max_length=32, required=True)
    password = forms.CharField(label="输入密码", max_length=256, widget=forms.PasswordInput())
    captcha = CaptchaField(label='验证码')


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label="输入密码", max_length=256, widget=forms.PasswordInput())
    password_confirm = forms.CharField(label="再次输入密码", max_length=256, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('userid', 'email', 'name')
