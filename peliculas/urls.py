from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies, name='getMovies'),
    path('getCharacters', views.getCharacters, name='getCharacters'),

]