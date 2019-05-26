from django.urls import path
from . import views

urlpatterns =  [
    path('', views.dashboard, name='dashboard'),
    path('<int:service_id>', views.serviceDetail, name="service_detail"),
]
