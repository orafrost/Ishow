from django.shortcuts import render
from .models import Server

# Create your views here.
def serverDetail(request, server_id=0):
    var = {}
    var["server"] = Server.objects.get(id=server_id)
    var["apps"] = var["server"].app_set.all()
    return render(request, 'server.html', var )
