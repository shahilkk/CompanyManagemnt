from django.shortcuts import render

# Create your views here.


def company_home(request):
    return render(request,'company/partials/master.html'),

def index(request):
    context={
        "is_index":True
    }
    return render(request,'company/partials/index.html',context)




def branch(request):
    context={
        "is_branch":True
    }
    return render(request,'company/branch/branch.html',context)

def addbranch(request):
    return render(request,'company/branch/addbranch.html')

def editbranch(request):
    return render(request,'company/branch/editbranch.html')

def branchview(request):
    return render(request,'company/branch/branchview.html')





def staff(request):
    context={
        "is_staff":True
    }
    return render(request,'company/staff/staff.html',context)

def addstaff(request):
  
    return render(request,'company/staff/addstaff.html',)


def invoice(request):
    context={
        "is_invoice":True
    }
    return render(request,'company/invoice/invoice.html',context)

def addinvoice(request):
    return render(request,'company/invoice/addinvoice.html') 

  



def expences(request):
    context={
        "is_expences":True
    }
    return render(request,'company/expences/expences.html',context)

def addexpences(request):
    return render(request,'company/expences/addexpences.html')  



def income(request):
    context={
        "is_income":True
    }
    return render(request,'company/income/income.html',context)

def addincome(request):
    return render(request,'company/income/addincome.html')  



def bank(request):
    context={
        "is_bank":True
    }
    return render(request,'company/bank/bank.html',context) 

 


def stafftransfer(request):
    context={
        "is_transfer":True
    }
    return render(request,'company/transfer/stafftransfer.html',context)    
    
def stocktransfer(request):
    context={
        "is_transfer":True
    }
    return render(request,'company/transfer/stocktransfer.html',context) 



def stock(request):
    context={
        "is_stock":True
    }
    return render(request,'company/stock/stock.html',context)

def branchstock(request):
    
    return render(request,'company/stock/branchstock.html')