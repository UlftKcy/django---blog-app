from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class Profile(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=154)
    image = models.ImageField(upload_to='media',blank=True,null=True)
    bio = models.CharField(max_length=200,blank=True)