from django.db import models
from Service.models import Section

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
    ip = models.CharField(max_length=15)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class App(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
