from email.policy import default
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(blank =True , null = True)
    price = models.DecimalField(max_digits = 1000 , decimal_places = 2 )
    summary = models.TextField(default = 'this is summary')
    