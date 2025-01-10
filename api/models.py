from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    enjoyment_value = models.IntegerField()
    cost = models.IntegerField()