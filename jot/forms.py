from pyexpat import model
from django import forms
import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    '''sign up form'''
    
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']