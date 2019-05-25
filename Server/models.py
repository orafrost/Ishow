from django.db import models
from Service.models import Service

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class App(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
