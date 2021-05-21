from django.core import validators
from django import forms
from .models import Brand, Cart, Checkout, Product
from django.core.exceptions import ValidationError

class FormProduct(forms.ModelForm):
    product_photo = forms.ImageField(required=False)
    class Meta:
        model = Product
        fields = ['name', 'code', 'stock', 'price', 'brand', 'network', 'display_details', 'camera_details', 'memory_details', 'battery_details' , 'product_photo']