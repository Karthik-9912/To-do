from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.
def register(request):

    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
            print("Succesful")
    context={
        'form':form
    }
    return render(request,'register.html',context)

def log_in(request):
    msg=''
    if request.method=='POST':
        username=request.POST.get('un')
        password=request.POST.get('pswd')
        try:
            a=User.objects.get(username=username)
        except:
            msg="User not found please register"
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('create')
        else:
            msg='password is incorrect'
    context={
        'msg':msg
    }
    return render(request,'login.html',context)

def log_out(request):
    logout(request)
    return redirect('login')