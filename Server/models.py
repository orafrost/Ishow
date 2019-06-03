from django.db import models
from Service.models import Section
from Client.models import Client

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30)
    ip = models.GenericIPAddressField(protocol='IPv4')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class ServerIntern(Server):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.section.name, self.name)

class ServerClient(Server):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.client.name, self.name)

class App(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
