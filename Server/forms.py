from django import forms
from .models import Server

class ServerForm(ModelForm):
    logo = forms.CharField(required=False)
    class Meta:
        model = Server
        fields = ['name', 'ip']
