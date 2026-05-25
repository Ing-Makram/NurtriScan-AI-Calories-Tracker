from rest_framework import viewsets, permissions
from .models import FoodImage, FoodItem
from .serializers import FoodImageSerializer, FoodItemSerializer
from ai.tasks import process_food_image_ai

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class FoodImageViewSet(viewsets.ModelViewSet):
    queryset = FoodImage.objects.all()
    serializer_class = FoodImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return FoodImage.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        process_food_image_ai.delay(instance.id)

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only items linked to the user's images
        return FoodItem.objects.filter(image__user=self.request.user)