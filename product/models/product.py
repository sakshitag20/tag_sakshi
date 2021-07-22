from django.db import models
import datetime

class Product(models.Model):
    name=models.CharField(max_length=100)
    weight=models.DecimalField(max_digits=10, decimal_places=4)
    created_at = models.DateField()
    updated_at= models.DateField()