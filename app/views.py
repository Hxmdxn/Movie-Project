from django.shortcuts import render,redirect,get_object_or_404
from .views import *
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

def home(request):
    return render(request,'homepg.html')

def movie_cards(request):
   mov=Cards.objects.all()
   dict={"mov": mov}
   return render(request,'cards.html',dict)

def movie_details(request,id):
    movie = get_object_or_404(Cards, id=id)
    d={'movie': movie}
    return render(request, 'movie_details.html', d)


def signin(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repeat_password=request.POST.get('r_password')
        number=request.POST.get('number')
        
        if password!=repeat_password:         
            messages.info(request,"password doesn't match")
            return redirect('/signin')
        
        if len(number) != 10:
            messages.info(request,"Invalid Phone Number")
            return redirect('/signin')
            
            
        try:
            if User.objects.get(username=name):
                messages.info(request,"User already exists")
                return redirect('/signin')
            
        except Exception as identifier:
            pass
        
        myuser=User.objects.create_user(name,email,password)
        myuser.save()
        messages.success(request,"User created, Please Login")
        return redirect('/login')
    return render(request,'register.html')

def login(request):
    if request.method=="POST":
        name=request.POST.get('username')
        password=request.POST.get('password')
        
        myuser=authenticate(username=name,password=password)
        if myuser is not None:
            auth_login(request,myuser)
            messages.success(request,"Login successful")
            return redirect("/movie_cards")
        else:
            messages.error(request,"Invalid credentials")
            return redirect("/login")
    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request,"Logged out successfully")
    return redirect("/movie_cards")
