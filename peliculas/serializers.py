from rest_framework import serializers
from .models import Movie, Character

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    class Meta:
        model = Character
        fields = ['id', 'name', 'actor', 'role', 'movie', 'movie_title']  # Incluye el campo extra


class GenreReportSerializer(serializers.Serializer):
    genre = serializers.CharField()
    count = serializers.IntegerField()
