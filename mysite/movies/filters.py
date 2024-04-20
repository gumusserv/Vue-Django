# from django_filters import rest_framework as filters
# from .models import Movie

# class MovieFilter(filters.FilterSet):
#     genre = filters.CharFilter(field_name='genre', lookup_expr='icontains')

#     class Meta:
#         model = Movie
#         fields = ['genre']


# filters.py
from django_filters import rest_framework as filters
from .models import Movie

class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    genre = filters.CharFilter(field_name='genre', lookup_expr='icontains')

    class Meta:
        model = Movie
        fields = ['title', 'genre']
