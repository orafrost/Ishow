from django.contrib import admin

# Register your models here.
from .models import Service, Section

admin.site.register(Service)
admin.site.register(Section)
