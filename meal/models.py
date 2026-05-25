from django.db import models
from users.models import AppUser
from food.models import FoodItem

class MealLog(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='meals')
    food_items = models.ManyToManyField(FoodItem)
    meal_time = models.DateTimeField()
    total_calories = models.PositiveIntegerField()
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)