from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='user:login')
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if password==confirmpassword:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists', extra_tags='username')
                return redirect('user:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists' ,extra_tags='email')
                return redirect('user:register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()

        else:
            messages.info(request,'password not match',extra_tags='password')
            return render(request,'register.html')
        return redirect('user:login')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'user is not registerd',extra_tags='user')
            return render(request,'login.html')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='user:login')
def profile(request):
    from django.contrib.auth.models import User



    return render(request,'profile.html')