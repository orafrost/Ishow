from django.urls import path
from . import views

urlpatterns =  [
    path('', views.dashboard, name='dashboard'),
#    path('/section', views.sectionList, name="section_list"),
#    path('/section/<int:section>', views.sectionDetail, name="section_detail"),
]
