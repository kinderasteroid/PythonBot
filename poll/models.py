from django.db import models

class color(models.Model):
    red = models.IntegerField(max_length=6000)
    green = models.IntegerField(max_length=6000)
    yellow= models.IntegerField(max_length=6000)
# Create your models here.
