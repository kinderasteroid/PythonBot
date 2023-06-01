from django.db import models

class register(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
# Create your models here.
