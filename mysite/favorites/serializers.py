# # favorites/serializers.py
# from rest_framework import serializers
# from .models import Favorite
# from movies.serializers import MovieSerializer
# from accounts.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']

# class FavoriteSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     movie = MovieSerializer(read_only=True)

#     class Meta:
#         model = Favorite
#         fields = ['user', 'movie']

# favorites/serializers.py
from rest_framework import serializers
from .models import Favorite
from movies.models import Movie

class FavoriteSerializer(serializers.ModelSerializer):
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source='movie', write_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'movie_id')
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        # 创建新的收藏实例，关联当前认证的用户和指定的电影
        user = self.context['request'].user
        movie = validated_data['movie']
        favorite, created = Favorite.objects.get_or_create(user=user, movie=movie)
        return favorite
