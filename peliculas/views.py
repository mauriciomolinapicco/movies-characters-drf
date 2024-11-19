from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import *
from .serializers import *

#GET ALL
@api_view(['GET'])
def getMovies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCharacters(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

#POST
@api_view(['POST'])
def addMovie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addCharacter(request):
    serializer = CharacterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#PUT
@api_view(['PUT'])
def updateMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
    
@api_view(['PUT'])
def updateCharacter(request, pk):
    character = Character.objects.get(pk=pk)
    serializer = CharacterSerializer(character, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


#DELETE
@api_view(['DELETE'])
def deleteMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return Response({"message":"Movie deleted with success"}, status=204)


@api_view(['DELETE'])
def deleteCharacter(request, pk):
    character = Character.objects.get(pk=pk)
    character.delete()
    return Response({"message": "Character deleted successfully"}, status=204)