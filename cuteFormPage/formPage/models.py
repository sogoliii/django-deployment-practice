from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class userProfileInfo(models.Model):
    """provide profile picture for User in admin"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank = True)
    picture = models.ImageField(upload_to = 'profile_pics' , blank = True)

    def __str__(self):
        return self.user.username


class userSignup(models.Model):
    """signup form model"""
    name = models.CharField(max_length = 264)
    lastname = models.CharField(max_length = 264)
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.name
