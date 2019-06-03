from django.shortcuts import render
from .models import Section

# Create your views here.
def dashboard(request):
    return render(request, 'index.html', {})

def serviceDetail(request, service_id=0):
    var = {}
    var["section_list"] = Section.objects.filter(service__id=service_id)
    return render(request, 'section.html', var)
