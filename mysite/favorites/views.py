from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Favorite, Movie, User

@api_view(['POST'])
def add_favorite(request):
    username = request.data.get('username')
    movie_id = request.data.get('movie_id')
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        user = User.objects.get(username=username)
        Favorite.objects.get_or_create(user=user, movie=movie)
        return Response({'message': 'Movie added to favorites'}, status=status.HTTP_201_CREATED)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def remove_favorite(request):
    movie_id = request.data.get('movie_id')
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        favorite = Favorite.objects.get(user=request.user, movie=movie)
        favorite.delete()
        return Response({'message': 'Movie removed from favorites'}, status=status.HTTP_204_NO_CONTENT)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    except Favorite.DoesNotExist:
        return Response({'error': 'Favorite not found'}, status=status.HTTP_404_NOT_FOUND)
