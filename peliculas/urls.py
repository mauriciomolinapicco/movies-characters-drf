from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies, name='getMovies'),
    path('getCharacters', views.getCharacters, name='getCharacters'),

    path('addMovie', views.addMovie),
    path('addCharacter', views.addCharacter),

    path('updateMovie/<int:pk>', views.updateMovie),
    path('updateCharacter/<int:pk>', views.updateMovie),

    path('deleteMovie/<int:pk>', views.deleteMovie),
    path('deleteCharacter/<int:pk>', views.deleteCharacter)
]