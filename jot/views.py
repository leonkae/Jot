from django.shortcuts import render

# Create your views here.

def home(request):
    '''home view'''
    return render(request, 'jotblog/home.html')

def login(request):
    '''login view'''
    return render(request, 'jotblog/login.html')

def signup(request):
    '''signup view'''
    return render(request, 'jotblog/signup.html')
