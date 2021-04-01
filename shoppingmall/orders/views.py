from django.shortcuts import render,redirect,HttpResponse
from.models import Mark
# Create your views here.
def education(request):
    obj=Mark.objects.get(id=1)
    return render(request,'education.html',{'ob':obj})
def education(request):
    obj2=Mark.objects.all()
    return render(request,'education.html',{'ob':obj2})
def crudhome(request):
    obj3=Mark.objects.all()
    return render(request,'crudhome.html',{'ob':obj3})
def delete(request,id):
   ob= Mark.objects.get(id=id).delete()
  # ob.delete()
   return redirect('orders:crudhome')
def edit(request,pk):
    if request.method == 'GET':
        ob=Mark.objects.get(id=pk)
        return render(request,'updatepage.html',{'ob':ob})
    else:
        s=request.POST['subject']
        m=request.POST['mark']
        st=request.POST['status']
        sid=request.POST['specialid']
        Mark.objects.filter(id=pk).update(subject=s,mark=m,status=st,specialid=sid)
        return redirect('orders:crudhome')

