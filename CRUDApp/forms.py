from django import forms
from django.contrib.auth.forms import UserCreationForm

from CRUDApp.models import Login, Profile

class LoginForm(UserCreationForm):
    username = forms.CharField(help_text=False, label='Email Address')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


