from django.contrib import admin

# Register your models here.
from .models import Server, App, ServerIntern, ServerClient

admin.site.register(ServerClient)
admin.site.register(ServerIntern)
admin.site.register(Server)
admin.site.register(App)
