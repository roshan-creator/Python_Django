from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    Description=models.TextField()
    Image=models.ImageField(upload_to='images/',blank=True,null=True)
    Assign=models.CharField(max_length=500,null=True)
    