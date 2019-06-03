from django.urls import path
from . import views

urlpatterns =  [
    path('<int:server_id>', views.serverDetail, name="server_detail"),
]
