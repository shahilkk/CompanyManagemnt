from django.shortcuts import render

# Create your views here.


def company_home(request):
    return render(request,'company/partials/master.html'),

def index(request):
    return render(request,'company/partials/index.html')




def branch(request):
    return render(request,'company/branch/branch.html')

def addbranch(request):
    return render(request,'company/branch/addbranch.html')

def editbranch(request):
    return render(request,'company/branch/editbranch.html')

def branchview(request):
    return render(request,'company/branch/branchview.html')





def staff(request):
    return render(request,'company/staff/staff.html')

def addstaff(request):
    return render(request,'company/staff/addstaff.html')


def invoice(request):
    return render(request,'company/invoice/invoice.html')

def addinvoice(request):
    return render(request,'company/invoice/addinvoice.html')   



def expences(request):
    return render(request,'company/expences/expences.html')

def addexpences(request):
    return render(request,'company/expences/addexpences.html')  

def income(request):
    return render(request,'company/income/income.html')

def addincome(request):
    return render(request,'company/income/addincome.html')  

def bank(request):
    return render(request,'company/bank/bank.html') 

 


def stafftransfer(request):
    return render(request,'company/transfer/stafftransfer.html')    
    
def stocktransfer(request):
    return render(request,'company/transfer/stocktransfer.html') 
