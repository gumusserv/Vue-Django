from django.urls import path
from . import views

urlpatterns = [
    # path('displayMovie', views.display_movies, name='display_movies'),
    path('api/movies/', views.MovieList.as_view(), name='api-movies'),
    path('api/movies/<int:id>/',  views.MovieDetailAPIView.as_view(), name='movie-detail'),
    path('api/genres/counts/', views.GenreCountsAPIView.as_view(), name='genre-counts'),
    path('api/ratings/counts/', views.RatingCountsAPIView.as_view(), name='rating-counts'),
]



