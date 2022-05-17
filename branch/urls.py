from django.urls import path
from . import views

app_name = 'branch'

urlpatterns = [
    path('master', views.master, name='master'),

    path('index', views.index, name='index'),



    path('customer', views.customer, name='customer'),
    path('addcustomer', views.addcustomer, name='addcustomer'),
    path('editcustomer', views.editcustomer, name='editcustomer'),



    path('employee', views.employee, name='employee'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('editemployee', views.editemployee, name='editemployee'),
]