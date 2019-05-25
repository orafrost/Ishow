from django.contrib import admin

# Register your models here.
from .models import Server, App

admin.site.register(Server)
admin.site.register(App)
