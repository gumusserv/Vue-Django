from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
