from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Brand(models.Model):
    brand = models.CharField( max_length=50, unique=True)
    def __str__(self):
        return self.brand

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    code = models.CharField(max_length=250, unique=True)
    stock = models.IntegerField()
    price = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    network = models.CharField(max_length=250)
    display_details = models.TextField()
    camera_details = models.TextField()
    memory_details = models.TextField()
    battery_details = models.TextField()
    product_photo = models.ImageField(upload_to="uploaded_image/products")
    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.product.name
    
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.TextField()
    phone = models.CharField(max_length=50)
    total = models.IntegerField()
    placed =models.BooleanField(default=False)
    shipped =models.BooleanField(default=False)
    # def __str__(self):
    #     return self.user.id

class Ordered(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()