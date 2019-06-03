from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=30)
    contract = models.CharField(max_length=30, default="")

    def __str__(self):
        return self.name
