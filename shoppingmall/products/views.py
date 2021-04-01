from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from .models import FirstTable

# Create your views here.
def index(request):
    return HttpResponse("<h1>welcome to my project</h1>")
def about(request):
    return HttpResponse("<h1>welcome to my about page</h1>")
def contact(request):
    return HttpResponse("<h1>my contact number is 8764567</h1>")
#def home(request):
   # return render(request,'home.html',{'h':'about hospital details'}) for change content
def login(request):
    return render(request,'login.html')
def reg(request):
    return render(request,'reg.html')
def onlineindex(request):
    return render(request,'onlineindex.html')
#def home(request):
   # obj1=FirstTable.objects.get(id=1)
    #return render(request, 'home.html', {'ob':obj1})
def home(request):

    obj=FirstTable.objects.all()
    return render(request, 'home.html', {'ob':obj})