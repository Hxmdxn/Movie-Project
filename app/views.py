from django.shortcuts import render,redirect
from .models import *

def home(request):
    return render(request,'homepg.html')

def movie_cards(request):
   mov=Cards.objects.all()
   dict={"mov": mov}
   return render(request,'cards.html',dict)