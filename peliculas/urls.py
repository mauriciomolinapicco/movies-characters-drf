from django.urls import path
from . import views

urlpatterns = [
    path('', views.getMovies, name='getMovies'),
    path('getCharacters', views.getCharacters, name='getCharacters'),

    path('addMovie', views.addMovie),
    path('addCharacter', views.addCharacter),

    path('updateMovie/<int:pk>', views.updateMovie),
    path('updateCharacter/<int:pk>', views.updateCharacter),

    path('deleteMovie/<int:pk>', views.deleteMovie),
    path('deleteCharacter/<int:pk>', views.deleteCharacter),

    path('api/login/', views.LoginView.as_view(), name='api_login'),
    path('api/logout/', views.LogoutView.as_view(), name='api_logout'),

    path('api/validate-token/', views.validate_token, name='validate-token'),

    path('api/movie-genre-report/', views.MovieGenreReportView.as_view(), name='movie_genre_report'),
]