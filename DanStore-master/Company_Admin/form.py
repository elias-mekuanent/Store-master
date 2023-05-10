import email
# from tkinter import Widget
from django import forms
from ..account.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class AddEmploye(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')
        