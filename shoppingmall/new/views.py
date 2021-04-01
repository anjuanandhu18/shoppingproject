
from django.shortcuts import render,redirect,HttpResponse
from.models import registerTable
from .forms import registerform
# Create your views here.
def register(request):
    if request.method=='GET':

        form=registerform()
        return render(request,'register.html',{'form':form})
    else:
        form=registerform(request.POST)
        form.save(request.POST)
        form=registerform()
        return render(request, 'register.html', {'form': form})
def delete(request,id):
    registerTable.object.get(id=id).delete()
    return render(request,'deletepage.html')

