from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FoodImageViewSet, FoodItemViewSet

router = DefaultRouter()
router.register(r'images', FoodImageViewSet)
router.register(r'items', FoodItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]