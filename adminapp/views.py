from django.shortcuts import render

# Create your views here.
def branch_home(request):
    return render(request,'admin/partials/base.html')
