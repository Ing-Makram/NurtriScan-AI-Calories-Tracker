from rest_framework import serializers
from .models import MealLog
from food.serializers import FoodItemSerializer

class MealLogSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, read_only=True)

    class Meta:
        model = MealLog
        fields = ['id', 'user', 'food_items', 'meal_time', 'total_calories', 'note', 'created_at']  