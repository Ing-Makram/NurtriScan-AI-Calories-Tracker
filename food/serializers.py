from rest_framework import serializers
from .models import FoodImage, FoodItem

class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = ['id', 'user', 'image', 'uploaded_at']

    def validate_image(self, value):
        if value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError("Image too large (max 5MB)")
        if not value.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            raise serializers.ValidationError("Only .jpg and .png files are allowed")
        return value

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id', 'image', 'name', 'calories', 'portion_size']