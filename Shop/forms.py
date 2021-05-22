from django.core import validators
from django import forms
from .models import Brand, Cart, Checkout, Product, Ordered
from django.core.exceptions import ValidationError

class FormProduct(forms.ModelForm):
    product_photo = forms.ImageField(required=False)
    class Meta:
        model = Product
        fields = ['name', 'code', 'stock', 'price', 'brand', 'network', 'display_details', 'camera_details', 'memory_details', 'battery_details' , 'product_photo']


class FormCart(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user', 'product', 'price', 'quantity']

class FormEditQty(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']

class FormCheckout(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['user', 'location', 'phone']


class FormOrdered(forms.ModelForm):
    class Meta:
        model = Ordered
        fields = ['checkout', 'product', 'price', 'quantity']