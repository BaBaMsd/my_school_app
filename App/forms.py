from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control my-2', 'placeholdar': 'Saisir admin nom'}))
    email = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control my-2', 'placeholdar': 'Saisir admin email'}))
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholdar': 'Saisir password'}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholdar': 'Confirm password'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
