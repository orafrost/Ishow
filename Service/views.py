from django.shortcuts import render
from .models import Section

# Create your views here.
def dashboard(request):
    return render(request, 'index.html', {})

def serviceDetail(request, service_id=0):
    try:
        section = Section.objects.filter(service__id=service_id)
    except:
        return HttpResponseNotFound('Error')
    return render(request, 'section.html', {"section_list":section})
