from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import FormProduct, FormCart
from django.db.models import Q
from django.shortcuts import redirect
from  django.contrib import messages
from django.db.models import Count
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    products = Product.objects.all()
    diction = {'products':products}
    return render(request, 'Shop/index.html', context = diction)

def wrong(request):
    diction = {}
    return render(request, 'Shop/wrong.html', context = diction)

def addproduct(request):
    brand = Brand.objects.all()
    myform = FormProduct()
    if request.method=="POST":
        myform = FormProduct(request.POST, request.FILES)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Product Added Successfully')
        
    diction = {'myform':myform, 'brand':brand}
    return render(request, 'Shop/panel/addproduct.html', context = diction)



def cart(request):
    carts = Cart.objects.all()
    # total = Cart.objects.aggregate(Sum('price'))
    total = sum(carts.values_list('price', flat=True))
    diction = {'carts':carts, 'total':total}
    return render(request, 'Shop/cart.html', context = diction)



def addtocart(request, id):
    if request.method=="POST":
        myform = FormCart(request.POST)
        product = Product.objects.get(pk=id)
        price = product.price
        adddata = Cart(user=request.user, product=product,price=price, quantity=1)
        adddata.save()
        messages.success(request, 'Product added')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deletethiscart(request, id):
    if request.method=="POST":
        delete_id = Cart.objects.get(pk=id)
        delete_id.delete()
        messages.success(request, 'Item Deleted')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))