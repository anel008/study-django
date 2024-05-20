from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    disc = models.TextField()
    img = models.ImageField(upload_to="images")
    