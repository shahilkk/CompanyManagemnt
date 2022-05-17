from django.shortcuts import render

# Create your views here.


def company_home(request):
    return render(request,'company/partials/master.html'),

def index(request):
    return render(request,'company/partials/index.html')




def branch(request):
    return render(request,'company/pages/branch.html')

def addbranch(request):
    return render(request,'company/pages/addbranch.html')

def editbranch(request):
    return render(request,'company/pages/editbranch.html')

def branchview(request):
    return render(request,'company/pages/branchview.html')





def staff(request):
    return render(request,'company/pages/staff.html')

def addstaff(request):
    return render(request,'company/pages/addstaff.html')


def invoice(request):
    return render(request,'company/pages/invoice.html')

def addinvoice(request):
    return render(request,'company/pages/addinvoice.html')   



def expences(request):
    return render(request,'company/pages/expences.html')

def addexpences(request):
    return render(request,'company/pages/addexpences.html')  

def income(request):
    return render(request,'company/pages/income.html')

def addincome(request):
    return render(request,'company/pages/addincome.html')  

def bank(request):
    return render(request,'company/pages/bank.html') 

def request(request):
    return render(request,'company/pages/request.html') 

    
