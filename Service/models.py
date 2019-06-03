from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=30)
    logo = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=10)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
