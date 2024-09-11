from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    size = models.CharField(max_length=255)
    description = models.TextField()


    