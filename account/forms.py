from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import CustomUser as User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите имя пользователя')
    email = forms.EmailField(label='Введите почту', widget=forms.EmailInput)
    password = forms.CharField(
        min_length=8, max_length=16, label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(
        min_length=8, max_length=16, label='Введите пароль снова', widget=forms.PasswordInput)

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise ValidationError('Пароли не совпадают')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Такая почта уже занята')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Такой username уже занят')
        return username


class UserLoginForm(forms.Form):
    username_or_email = forms.CharField(
        label='Введите имя пользователя или почту')
    password = forms.CharField(
        widget=forms.PasswordInput, label='Введите пароль')

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get("username_or_email")
        password = cleaned_data.get("password")

        if username_or_email and password:
            return cleaned_data
        else:
            raise forms.ValidationError("Заполните все поля")
