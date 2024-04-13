from django.contrib import messages, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.models import User
from cart_movie.models import Movies,Genres
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    current_year = datetime.now().year
    YEARS_CHOICES = [year for year in range(current_year, current_year - 50, -1)]
    movie=Movies.objects.all()
    context={
        'year':YEARS_CHOICES,
        'movie':movie
    }
    return render(request,'index.html',{'context':context})


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


def profile(request):
    return render(request,'profile.html')


def edit_profile(request,id):

    user=User.objects.get(id=id)
    user_details={
        'status':True,
        'user':user

    }

    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']

        user.first_name=firstname
        user.last_name=lastname
        user.email=email

        user.save()
        return redirect('user:profile')

    return render(request,'profile.html',{'user_details':user_details})