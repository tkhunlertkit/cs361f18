from django.db import models

# Create your models here.
class Data(models.Model):

    a = models.CharField(max_length=20)