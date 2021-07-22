from django.db import models
import datetime

class Post(models.Model):
    user=models.CharField(max_length=100)
    text=models.CharField(max_length=500)
    created_at = models.DateField()
    updated_at= models.DateField()
