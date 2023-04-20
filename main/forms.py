from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        #unique=True,

        validators=[username_validator],
        error_messages={
            "unique": "Такой логин уже существует. Давай другой.",
        }, label='Логин')

    class Meta:
        model = User
        fields = ['username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Логин')
    password = forms.CharField(max_length=150, label='Пароль')




