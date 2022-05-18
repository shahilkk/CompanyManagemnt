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


def profitandloss(request):
    return render(request,'branch/profitandloss.html')


def payment(request):
    return render(request,'branch/payment.html')

def expense(request):
    return render(request,'branch/expenses/expense.html')    

def addexpense(request):
    return render(request,'branch/expenses/addexpenses.html')     



def income(request):
    return render(request,'branch/income.html')



def preview(request):
    return render(request,'branch/preview.html')


def search(request):
    return render(request,'branch/stocksearch.html')


def estimate(request):
    return render(request,'branch/billing/estimate.html')


def invoice(request):
    return render(request,'branch/billing/invoice.html')


def bill(request):
    return render(request,'branch/billing/bill.html')


def stockrequest(request):
    return render(request,'branch/request/stockrequest.html')


def staffrequest(request):
    return render(request,'branch/request/staffrequest.html')
    