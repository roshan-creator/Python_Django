from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    captcha = CaptchaField()


    class Meta:
        model = User
        fields = ['username','email','password1','password2']