from django.db import models
from users.models import AppUser

class FoodImage(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='food_images')
    image = models.ImageField(upload_to='food_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} by {self.user.username}"

class FoodItem(models.Model):
    image = models.ForeignKey(FoodImage, on_delete=models.CASCADE, related_name='food_items')
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    portion_size = models.FloatField()  # in grams

    def __str__(self):
        return self.name