from django.db import models

class Ticket(models.Model):
    datetime = models.DateTimeField()
    location = models.CharField(max_length=20)
