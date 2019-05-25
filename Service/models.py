from django.db import models

# Create your models here.
class Service(models.Model):
    first = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
