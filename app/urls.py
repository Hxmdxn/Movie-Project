from django.contrib import admin
from django.urls import path
from . import views 
from . models import *


urlpatterns = [
    path('', views.home, name='home'),
    path('movie_cards', views.movie_cards, name='movie_cards'),
    path('movie/<int:id>/', views.movie_details, name='movie_details'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
]