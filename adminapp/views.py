from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request,'admin/partials/base.html')


def index(request):
    return render(request,'admin/index.html')

def addproject(request):
    return render(request,'admin/project/addproject.html')


def listproject(request):
    return render(request,'admin/project/listproject.html')    
       

def addbranch(request):
    return render(request,'admin/branches/addbranch.html')       


def listbranch(request):
    return render(request,'admin/branches/listbranch.html')  


def viewbranch(request):
    return render(request,'admin/branches/viewbranch.html') 


def employeelist(request):
    return render(request,'admin/employee/employelist.html')


def team(request):
    return render(request,'admin/team.html')    
