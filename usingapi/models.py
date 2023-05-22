from django.db import models

# Create your models here.
class Product_View(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=200)
    total_buyers=models.IntegerField()