from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from siteusers.models import SiteUser


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'input-group-text',
                                                             'style': 'min-width: 100%'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'input-group-text',
                                                            'style': 'min-width: 100%'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'input-group-text',
                                                                  'style': 'min-width: 100%'}))
    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'input-group-text',
                                                                  'style': 'min-width: 100%'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'input-group-text',
                                                             'style': 'min-width: 100%'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'input-group-text',
                                                                 'style': 'min-width: 100%'}))

    class Meta:
        model = SiteUser
        fields = ('username', 'password')