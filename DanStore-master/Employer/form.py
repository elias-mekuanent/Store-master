from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
class passwordform(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('old_password','new_password1','new_password2')
        
        