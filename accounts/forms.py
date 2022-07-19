from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1']
        
class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget= forms.TextInput(attrs={'id':'input_username'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput())
