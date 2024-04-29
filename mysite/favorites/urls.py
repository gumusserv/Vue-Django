from django.urls import path
from .views import add_favorite, remove_favorite, check_favorite, UserFavoriteListView

urlpatterns = [
    path('api/favorites/add/', add_favorite, name='add-favorite'),
    path('api/favorites/remove/', remove_favorite, name='remove-favorite'),
    path('api/favorites/check/<str:username>/<int:movie_id>/', check_favorite, name='check-favorite'),
    path('api/favorites/get_favorites/', UserFavoriteListView.as_view(), name='user-favorite-list'),
]
