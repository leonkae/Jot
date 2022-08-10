from django.shortcuts import render

# Create your views here.

def home(request):
    '''home view'''
    return render(request, 'jotblog/home.html')