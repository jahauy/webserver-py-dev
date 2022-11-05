# app/forms.py

from django import forms
from .models import User
from captcha.fields import CaptchaField


class UserLoginForm(forms.ModelForm):
    captcha = CaptchaField(label='验证码')

    class Meta:
        model = User
        fields = ('userid', 'password')


# class UserLoginForm(forms.Form):
#     captcha = CaptchaField(label='验证码')
#     userid = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput())
#     password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput())

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
