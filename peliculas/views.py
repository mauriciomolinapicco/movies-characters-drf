from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Movie, Character
from .serializers import MovieSerializer, CharacterSerializer

# GET ALL
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMovies(request):
    try:
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getCharacters(request):
    try:
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        return Response(serializer.data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# POST
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMovie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=201)
        except IntegrityError as e:
            return Response({"error": "Error de integridad: " + str(e)}, status=400)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addCharacter(request):
    serializer = CharacterSerializer(data=request.data)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=201)
        except IntegrityError as e:
            return Response({"error": "Error de integridad: " + str(e)}, status=400)
    return Response(serializer.errors, status=400)


# PUT
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMovie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieSerializer(movie, data=request.data, partial=True)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateCharacter(request, pk):
    character = get_object_or_404(Character, pk=pk)
    serializer = CharacterSerializer(character, data=request.data, partial=True)
    if serializer.is_valid():
        try:
            serializer.save()
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    return Response(serializer.errors, status=400)


# DELETE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteMovie(request, pk):
    try:
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response({"message": "Pelicula eliminada con exito"}, status=204)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteCharacter(request, pk):
    try:
        character = get_object_or_404(Character, pk=pk)
        character.delete()
        return Response({"message": "Personaje eliminado con exito"}, status=204)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


# Login and logout
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        return Response({"error": "Credenciales invalidas"}, status=401)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Se hizo logout con exito!"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def validate_token(request):
    return Response({'detail': 'Token válido'}, status=200)
