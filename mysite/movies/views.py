from rest_framework import generics, filters, status
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from .models import Movie
from .serializers import MovieSerializer
from .filters import MovieFilter  # 确保导入你的自定义过滤器类
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count, Q, Case, When, Value, IntegerField
from rest_framework.filters import OrderingFilter
import django_filters


class MoviePagination(PageNumberPagination):
    page_size = 9  # 默认每页12个
    page_size_query_param = 'page_size'  # 允许客户端通过查询参数page_size来请求不同的页大小
    max_page_size = 100  # 最大页大小限制为100


class MovieList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = MovieFilter
    pagination_class = MoviePagination  # 使用自定义的分页类

    def get_queryset(self):
        """
        Optionally customizes the default query by adding sorting based on the search and rating.
        """
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', '')

        if search_query:
            # Case when search query is provided: sort by relevance (simulated here using an annotation)
            # and then by rating. Assume 'popularity' is a field representing search relevance.
            queryset = queryset.annotate(
                relevance=Case(
                    When(title__icontains=search_query, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField()
                )
            ).order_by('-relevance', '-historical_rating')
        else:
            # If no search query, sort simply by rating
            queryset = queryset.order_by('-historical_rating')
        
        return queryset



class MovieDetailAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(movie_id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    


class GenreCountsAPIView(APIView):
    def get(self, request):
        # 获取额外的筛选参数，例如搜索词、已选择的题材、评分范围和年份范围
        search_query = request.query_params.get('search', '')
        selected_genres = request.query_params.get('genres', '').split(',')
        rating_min = request.query_params.get('ratingMin', None)  # 获取最低评分的查询参数
        year_min = request.query_params.get('year_min', None)
        year_max = request.query_params.get('year_max', None)
       

        # 定义所有需要显示计数的题材
        genres = ['剧情', '科幻', '动画', '爱情', '喜剧', '动作']
        genre_counts = []

        # 对于每个题材，计算考虑当前筛选后的电影数量
        for genre in genres:
            query = Movie.objects.all()
            if search_query:
                query = query.filter(title__icontains=search_query)
            if selected_genres:
                # 应用其他已选择的题材为额外的筛选条件
                for other_genre in selected_genres:
                    if other_genre and other_genre != genre:
                        query = query.filter(genre__icontains=other_genre)
            if rating_min is not None:  # 应用评分过滤条件
                query = query.filter(historical_rating__gte=rating_min)
            if year_min:
                query = query.filter(year__gte=year_min)
            if year_max:
                query = query.filter(year__lte=year_max)
           

            # 计算当前条件下每个题材的电影数量
            count = query.filter(genre__icontains=genre).count()
            genre_counts.append({'name': genre, 'count': count})

        return Response({'genres': genre_counts}, status=status.HTTP_200_OK)
    
class RatingCountsAPIView(APIView):
    def get(self, request):
        # 获取额外的筛选参数
        search_query = request.query_params.get('search', '')
        selected_genres = request.query_params.get('genres', '').split(',')
        year_min = request.query_params.get('year_min', None)
        year_max = request.query_params.get('year_max', None)

        # 定义评分等级
        ratings = [0, 1, 2, 3, 4]
        rating_counts = []

        for rating in ratings:
            query = Movie.objects.all()
            if search_query:
                query = query.filter(title__icontains=search_query)
            if selected_genres:
                for genre in selected_genres:
                    query = query.filter(genre__icontains=genre)
            if year_min:
                query = query.filter(year__gte=year_min)
            if year_max:
                query = query.filter(year__lte=year_max)

            count = query.filter(historical_rating__gte=rating).count()
            rating_counts.append({'rating': rating, 'count': count})

        return Response({'ratings': rating_counts})



