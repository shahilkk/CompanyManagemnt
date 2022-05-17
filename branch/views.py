from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request,'branch/partials/base.html')


def index(request):
    return render(request,'branch/index.html')    



def customer(request):
    return render(request,'branch/customer/customer.html')


def addcustomer(request):
    return render(request,'branch/customer/addcustomer.html')

def editcustomer(request):
    return render(request,'branch/customer/editcustomer.html')    




def employee(request):
    return render(request,'branch/employees/employee.html')


def addemployee(request):
    return render(request,'branch/employees/addemploye.html')

def editemployee(request):
    return render(request,'branch/employees/editemploye.html')


