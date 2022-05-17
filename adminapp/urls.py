from django.urls import path
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('master', views.master, name='master'),

    path('index', views.index, name='index'),

    path('addproject', views.addproject, name='addproject'),
    path('listproject', views.listproject, name='listproject'),

    path('addbranch', views.addbranch, name='addbranch'),
    path('listbranch', views.listbranch, name='listbranch'),
    path('viewbranch', views.viewbranch, name='viewbranch'),

    path('employeelist', views.employeelist, name='employeelist'),


    path('team', views.team, name='team'),

]