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
