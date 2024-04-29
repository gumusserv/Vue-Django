from rest_framework import serializers
from .models import Movie, Comment, User

class UserMovieCommentSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    comment_text = serializers.CharField(source='comment', read_only=True)
    movie_id = serializers.IntegerField(source='movie.movie_id', read_only=True)
    username = serializers.CharField(source = 'user.username', read_only = True)

    class Meta:
        model = Comment
        fields = ('movie_title', 'comment_text', 'movie_id', 'username')
