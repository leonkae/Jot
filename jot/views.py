from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *


# Create your views here.

def home(request):
    '''home view'''
    return render(request, 'jotblog/home.html')

def login(request):
    '''login view'''
    return render(request, 'jotblog/login.html')

def signup(request):
    '''signup view'''
    if request.user.is_authenticated:
        return redirect ('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username =form.cleaned_data.get('username')
                created_user = form.save()
                Profile.objects.get_or_create(user=created_user)
                messages.success(request,'Account for' + username +'created Successfully')
                return redirect ('login')
        
        context = {'form':form}
        return render(request, 'jotblog/signup.html', context)
