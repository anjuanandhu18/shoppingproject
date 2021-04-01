from django.shortcuts import render,redirect,HttpResponse
from .models import formtable

# Create your views here.
def log1(request):
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        date=request.POST['date']
        formtable.objects.create(name=name,age=age,date=date)
        return render(request,'log1.html')
    else:
        return render(request,'log1.html')

