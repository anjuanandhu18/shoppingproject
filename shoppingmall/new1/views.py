from django.shortcuts import render,redirect,HttpResponse
from .models import new1table


# Create your views here.
#this is my insert page code
def log(request):
    if request.method == 'POST':
        user=request.POST['user']
        password=request.POST['password']
        new1table.objects.create(user=user,password=password)
        return render(request,'log.html')
    else:
        return render(request, 'log.html')
