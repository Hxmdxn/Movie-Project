from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from . models import *


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.movie_cards, name='movie_cards'),
    path('movie/<int:id>/', views.movie_details, name='movie_details'),
    path('imdb_movie/<int:id>/', views.imdb_movie_details, name='imdb_movie_details'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('search/', views.search_movies, name='search_movies'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)