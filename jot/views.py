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

def loginPage(request):
    '''login view'''
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            print(username,password,user)
            if user is not None:
                login(request,user)
                return redirect ('home')
            else:
                messages.info(request,'Check username or password !')
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

def postBlog(request):
    '''post blog view'''
    
    posts = Blogpost.objects.all()
    current_user = request.user
    user_profile = get_object_or_404(Profile,user = current_user)
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        print('data',data)
        print('image', image)
        
        post = Blogpost.objects.create(
            title = data['title'],
            blog = data['blog'],
            image = image,
            profile =user_profile ,
        )
        post.save()
        return redirect('home')
    
    return render(request,'jotblog/post.html')