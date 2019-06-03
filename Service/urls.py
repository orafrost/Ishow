from django.urls import path
from . import views

urlpatterns =  [
    path('<int:service_id>', views.serviceDetail, name="service_detail"),
]
