from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.company_home, name='companyhome'),
    path('index', views.index, name='index'),


    path('branch', views.branch, name='branch'),
    path('branchview', views.branchview, name='branchview'), 
    path('addbranch',views.addbranch,name='addbranch'),
    path('editbranch',views.editbranch,name='editbranch'),

    path('staff', views.staff, name='staff'),
    path('addstaff',views.addstaff, name='addstaff'),

    path('invoice',views.invoice,name='invoice'),
    path('addinvoice',views.addinvoice,name='addinvoice'),
    path('expences',views.expences,name='expences'),
    path('addexpences',views.addexpences,name='addexpences'),

    
    path('income',views.income,name='income'),
    path('addincome',views.addincome,name='addincome'),

    path('bank',views.bank,name='bank'),
   
    path('request',views.request,name='request'),
    
]