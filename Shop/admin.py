from django.contrib import admin
from .models import Brand, Product, Cart, Checkout

# Register your models here.

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','brand')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'code', 'brand', 'stock', 'price', 'network', 'display_details', 'camera_details', 'memory_details', 'battery_details', 'product_photo' )

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'price', 'quantity')

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'phone', 'placed', 'shipped')