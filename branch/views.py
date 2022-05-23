from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request,'branch/partials/base.html')


def index(request):
    context={
        "is_index":True
    }
    return render(request,'branch/index.html',context)    



def customer(request):
    context={
        "is_customer":True
    }
    return render(request,'branch/customer/customer.html',context)

def addcustomer(request):
    context={
        "is_customer":True
    }
    return render(request,'branch/customer/addcustomer.html',context)

def editcustomer(request):
    context={
        "is_customer":True
    }
    return render(request,'branch/customer/editcustomer.html',context)    




def employee(request):
    context={
        "is_employee":True
    }
    return render(request,'branch/employees/employee.html',context)


def addemployee(request):
    context={
        "is_employee":True
    }
    return render(request,'branch/employees/addemploye.html',context)

def editemployee(request):
    context={
        "is_employee":True
    }
    return render(request,'branch/employees/editemploye.html',context)


def profitandloss(request):
    context={
        "is_profitandloss":True
    }
    return render(request,'branch/profitandloss.html',context)


def payment(request):
    context={
        "is_payment":True
    }
    return render(request,'branch/payment.html',context)

def expense(request):
    context={
        "is_expenses":True
    }
    return render(request,'branch/expenses/expense.html',context)    

def addexpense(request):
    context={
        "is_expenses":True
    }
    return render(request,'branch/expenses/addexpenses.html',context)     



def income(request):
    context={
        "is_income":True
    }
    return render(request,'branch/income.html',context)



def preview(request):
    context={
        "is_preview":True
    }
    return render(request,'branch/preview.html',context)


def search(request):
    context={
        "is_search":True
    }
    return render(request,'branch/stocksearch.html',context)


def estimate(request):
    context={
        "is_estimate":True
    }
    return render(request,'branch/billing/estimate.html',context)


def invoice(request):
    context={
        "is_invoice":True
    }
    return render(request,'branch/billing/invoice.html',context)


def bill(request):
    context={
        "is_bill":True
    }
    return render(request,'branch/billing/bill.html',context)


def stockrequest(request):
    context={
        "is_bill":True
    }
    return render(request,'branch/request/stockrequest.html',context)


def staffrequest(request):
    context={
        "is_bill":True
    }
    return render(request,'branch/request/staffrequest.html',context)


def product(request):
    context={
        "is_product":True
    }
    return render(request,'branch/product/product.html',context)


def addproduct(request):
    context={
        "is_product":True
    }
    return render(request,'branch/product/addproduct.html',context)


def editproduct(request):
    context={
        "is_product":True
    }
    return render(request,'branch/product/editproduct.html',context)


def purchaselist(request):
    context={
        "is_purchaselist":True
    }
    return render(request,'branch/purchaselist.html',context)



def master(request):
    return render(request,'branch/master.html')
    