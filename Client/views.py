from django.shortcuts import render
from .models import Client

# Create your views here.
def clientDetail(request):
    var = {}
    var["section_list"] = Client.objects.all()
    return render(request, 'client.html', var)
