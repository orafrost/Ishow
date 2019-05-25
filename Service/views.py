from django.shortcuts import render
from .models import Service

# Create your views here.
def dashboard(request):
    return render(request, 'index.html', {})

def sectionList(request, service_id):
    try:
        section = Service.objects.filter(section__id=service_id)
    except:
        section = []
    render(request, 'section.html', {})

def sectionDetail(request, id):
    pass
