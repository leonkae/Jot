from cgitb import text
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    '''profile model'''
    bio = models.TextField(max_length=255)
    prophoto = models.ImageField(upload_to='profile/', default = 'image.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    following = models.ManyToManyField(User, related_name ='following')
    followers = models.ManyToManyField(User, related_name= 'followers')  
    
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    user_post = models.ForeignKey('Blogpost', on_delete=models.CASCADE,related_name = 'user_comments' )    
    
    def __str__(self):
        return f'{self.user.username} Blogpost'

class Blogpost(models.Model):
    '''blogpost model'''
    title = models.CharField(max_length=255)
    blog = models.TextField()
    image = models.ImageField(upload_to='blogpost/',default='img.jpg')
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_post')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment,blank=True)
    
    
    def __str__(self):
        return f'{self.profile.user.username} Blogpost'
    
        
    