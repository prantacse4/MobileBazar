from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.TextField(default=None)
    phone = models.CharField( max_length=50, unique=True, default=None)
    image = models.ImageField(upload_to="uploaded_image/user")