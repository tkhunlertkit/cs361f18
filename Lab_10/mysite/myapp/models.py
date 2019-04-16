from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)

class User(models.Model):
    name = models.CharField(max_length=20)
    items = models.ManyToManyField(Item)
    new = models.CharField(max_length=10, default="hello")
    new2 = models.CharField(max_length=10)
