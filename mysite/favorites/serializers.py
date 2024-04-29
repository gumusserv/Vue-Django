from rest_framework import serializers
from .models import Favorite
from movies.serializers import MovieSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()  # 嵌套使用电影的序列化器

    class Meta:
        model = Favorite
        fields = ['movie']
