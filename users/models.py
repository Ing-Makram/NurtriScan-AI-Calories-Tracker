from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    # You can extend with more fields as needed
    pass

class DeviceSession(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    device_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)