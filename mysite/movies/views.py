# from django.shortcuts import render
# from rest_framework import generics, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Movie
# from .serializers import MovieSerializer

# def display_movies(request):
#     movies = Movie.objects.all()
#     return render(request, 'display_movies.html', {'movies': movies})




# class MovieList(generics.ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ['genre']
#     ordering_fields = ['title', 'year']

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieSerializer
from .filters import MovieFilter  # 确保导入你的自定义过滤器类
from rest_framework.views import APIView
from rest_framework.response import Response


class MoviePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = ['genre']
    filterset_class = MovieFilter
    pagination_class = MoviePagination
    ordering_fields = ['title', 'year']



class MovieDetailAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(movie_id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)



