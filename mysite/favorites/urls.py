from django.urls import path
from .views import FavoriteListView, FavoriteListCreateView

urlpatterns = [
    path('', FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
]
