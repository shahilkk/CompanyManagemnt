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


    path('profitandloss', views.profitandloss, name='profitandloss'),



    path('payment', views.payment, name='payment'),

    path('expense', views.expense, name='expense'),
    path('addexpense', views.addexpense, name='addexpense'),


    path('income', views.income, name='income'),


    path('preview', views.preview, name='preview'),

    path('search', views.search, name='search'),


    path('estimate', views.estimate, name='estimate'),
    path('invoice', views.invoice, name='invoice'),
    path('bill', views.bill, name='bill'),


    path('staffrequest', views.staffrequest, name='staffrequest'),
    path('stockrequest', views.stockrequest, name='stockrequest'),

   
    








    
]