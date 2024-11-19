from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import *
from .serializers import *

#GET ALL
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMovies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCharacters(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data)

#POST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMovie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCharacter(request):
    serializer = CharacterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#PUT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCharacter(request, pk):
    character = Character.objects.get(pk=pk)
    serializer = CharacterSerializer(character, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


#DELETE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteMovie(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return Response({"message":"Movie deleted with success"}, status=204)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCharacter(request, pk):
    character = Character.objects.get(pk=pk)
    character.delete()
    return Response({"message": "Character deleted successfully"}, status=204)


# Login and logout 
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            # Generar o recuperar el token
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        return Response({"error": "Invalid credentials"}, status=401)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Elimina el token
        request.user.auth_token.delete()
        return Response({"message": "Logout successful!"}, status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def validate_token(request):
    return Response({'detail': 'Token válido'}, status=200)
