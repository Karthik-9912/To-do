from django.shortcuts import render , redirect
from .models import To_Do
# Create your views here.

def create(request):
    if request.method=='POST':
        task=request.POST.get('task')
        description=request.POST.get('desc')
        To_Do.objects.create(task=task,desc=description)
        return redirect('display')
    return render(request,'create.html')

def display(request):
    data=To_Do.objects.all()
    context={
        'data':data
    }
    return render(request,'display.html',context)

def single(request,pk):
    data=To_Do.objects.get(id=pk)
    context={
        'data':data
    }
    return render(request,'single.html',context)

def edit(request,vk):
    data=To_Do.objects.get(id=vk)
    a=True
    if request.method=='POST':
        task=request.POST.get('task')
        description=request.POST.get('desc')
        # print(task,description)
        data.task, data.desc=task,description
        data.save()
        return redirect('display')
    context={
        'data':data,
        'a':a
    }  
    return render(request,'update.html',context)


def delete(request,dl):
    data=To_Do.objects.get(id=dl)
    data.delete()
    return redirect('display')
