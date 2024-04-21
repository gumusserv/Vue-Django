from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Comment, Movie, User

@api_view(['POST'])
def add_comment(request):
    username = request.data.get('username')
    movie_id = request.data.get('movie_id')
    comment = request.data.get('comment')
    try:
        movie = Movie.objects.get(movie_id=movie_id)
        user = User.objects.get(username=username)
        newComment, created = Comment.objects.get_or_create(user=user, movie=movie)
        newComment.comment = comment
        newComment.save()
        return Response({'message': 'Add Comment Successfully'}, status=status.HTTP_201_CREATED)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def add_rating(request):
    username = request.data.get('username')
    movie_id = request.data.get('movie_id')
    rating = request.data.get('rating')
    allowed_ratings = {0, 1, 2, 3, 4, 5}  # 定义允许的评分值

    try:
        movie = Movie.objects.get(movie_id=movie_id)
        user = User.objects.get(username=username)
        newComment, created = Comment.objects.get_or_create(user=user, movie=movie)

        # 验证评分是否在允许的范围内
        if rating in allowed_ratings:
            newComment.rating = rating
            newComment.save()
            return Response({'message': 'Add Rating Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid rating value'}, status=status.HTTP_400_BAD_REQUEST)

    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)



# @api_view(['DELETE'])
@api_view(['POST'])
def delete_comment(request):
    username = request.data.get('username')
    movie_id = request.data.get('movie_id')

    try:
        movie = Movie.objects.get(movie_id=movie_id)
        user = User.objects.get(username=username)
        oldComment, created = Comment.objects.get_or_create(user=user, movie=movie)
        oldComment.comment = None  # Optionally clear the comment text or delete the entire object
        oldComment.save()
        return Response({'message': 'Comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_rating(request):
    username = request.data.get('username')
    movie_id = request.data.get('movie_id')

    try:
        movie = Movie.objects.get(movie_id=movie_id)
        user = User.objects.get(username=username)
        comment = Comment.objects.get(user=user, movie=movie)
        comment.rating = None  # Clear the rating field
        comment.save()
        return Response({'message': 'Rating deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Comment.DoesNotExist:
        return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
