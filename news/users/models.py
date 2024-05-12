from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    is_author = models.BooleanField(default=False)
    age = models.PositiveIntegerField(null=True,blank=True)
    email = models.EmailField(max_length=254,unique=True,null=False,blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']