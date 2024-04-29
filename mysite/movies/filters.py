


# filters.py
import django_filters
from .models import Movie
from django.db import models

class MovieFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    genres = django_filters.CharFilter(method='filter_genres')
    ratingMin = django_filters.NumberFilter(field_name='historical_rating', lookup_expr='gte')
    year_min = django_filters.NumberFilter(field_name='year', lookup_expr='gte')  # 最小年份
    year_max = django_filters.NumberFilter(field_name='year', lookup_expr='lte')  # 最大年份


    class Meta:
        model = Movie
        fields = ['search', 'genres', 'ratingMin', 'year']

    def filter_genres(self, queryset, name, value):
        if value:
            genres = value.split(',')
            queries = [models.Q(genre__icontains=genre) for genre in genres]
            query = queries.pop()
            for item in queries:
                query &= item  # OR 条件
            return queryset.filter(query)
        return queryset

