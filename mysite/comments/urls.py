from django.urls import path
from .views import *

urlpatterns = [
    path('api/comment/add-comment/', add_comment, name='add-comment'),
    path('api/comment/add-rating/', add_rating, name='add-rating'),
    path('api/comment/delete-comment/', delete_comment, name='delete-comment'),
    path('api/comment/delete-rating/', delete_rating, name='delete-rating'),
    # path('api/comment/remove/', remove_favorite, name='remove-favorite'),
]