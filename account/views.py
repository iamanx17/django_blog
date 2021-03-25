from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

#register section
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username has already taken')
                return render(request,'index/register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email has already taken')
                return render(request,'index/register.html')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password1)
                user.save()
                messages.success(request,'User has been successfully created')
                return render(request,'index/register.html')
        else:
            messages.error(request,'Password not matched')
            return render(request,'index/register.html')
    return render(request,'index/register.html')

#login section
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['passwordx']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'User data not found')
            return render(request,'index/login.html')

    return render(request,'index/login.html')

#logout section
def logout(request):
    auth.logout(request)
    return redirect('/')