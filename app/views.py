from django.shortcuts import render,redirect,get_object_or_404
from .views import *
from .models import * 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.utils.safestring import mark_safe

def home(request):
    return render(request,'homepg.html')

def movie_cards(request):
    mov = Cards.objects.all()
    imdbb = imdb.objects.all()
    
    context = {
        'mov': mov,
        'imdbb': imdbb,
    }
    return render(request, 'cards.html', context)
    
    
def movie_details(request, id):
    movie = get_object_or_404(Cards, id=id)
    mov = Cards.objects.all()
    movie.detailed_description=mark_safe(movie.detailed_description)
    
    context = {
        'movie': movie,
        'mov': mov,
    }
    return render(request, 'movie_details.html', context)

def imdb_movie_details(request, id):
    movie = get_object_or_404(imdb, id=id)
    imdbb = imdb.objects.all()
    mov = Cards.objects.all()
    

    context = {
        'moviee': movie,
        'imdbb': imdbb,
        'mov': mov,
    }
    return render(request, 'imdb_movie_details.html', context)

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
            return redirect('/')
        else:
            messages.error(request,"Invalid credentials")
            return redirect("/login")
    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('/')

def search_movies(request):
    query = request.GET.get('q')  
    cards = Cards.objects.all() 

    if query:
        cards = Cards.objects.filter(name__icontains=query)  

    return render(request, 'search.html', {'cards': cards, 'query': query})