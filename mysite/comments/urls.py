from django.urls import path
from .views import *

urlpatterns = [
    path('api/comment/add-comment/', add_comment, name='add-comment'),
    path('api/comment/add-rating/', add_rating, name='add-rating'),
    path('api/comment/delete-comment/', delete_comment, name='delete-comment'),
    path('api/comment/delete-rating/', delete_rating, name='delete-rating'),
    path('api/comment/get_comments/', UserCommentListView.as_view(), name='user-comments-list'),
    path('api/comment/get_comments_byMovies/', MovieCommentListView.as_view(), name='movie-comments-list'),
    path('api/rating/<str:username>/<int:movie_id>/', get_user_rating, name='get_user_rating'),
    path('api/comment/<str:username>/<int:movie_id>/', get_user_comment, name='get_user_comment'),
]