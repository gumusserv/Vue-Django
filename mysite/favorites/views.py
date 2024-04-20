from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Favorite
from movies.models import Movie
from .serializers import FavoriteSerializer  # 你需要为Favorite模型创建一个序列化器

class FavoriteListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)

    def post(self, request):
        movie_id = request.data.get('movie_id')
        movie = Movie.objects.get(movie_id=movie_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, movie=movie)
        if created:
            return Response({"status": "success"}, status=status.HTTP_201_CREATED)
        return Response({"status": "favorite already exists"}, status=status.HTTP_409_CONFLICT)

    def delete(self, request):
        movie_id = request.data.get('movie_id')
        movie = Movie.objects.get(movie_id=movie_id)
        favorite = Favorite.objects.filter(user=request.user, movie=movie)
        favorite.delete()
        return Response({"status": "removed"}, status=status.HTTP_204_NO_CONTENT)
    
class FavoriteListCreateView(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 返回当前用户的所有收藏
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 当创建新的收藏时, 自动设置用户为当前请求的用户
        serializer.save(user=self.request.user)
