from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import FormProduct, FormCart, FormEditQty, FormCheckout, FormOrdered,FormProStock
from django.db.models import Q
from django.shortcuts import redirect
from  django.contrib import messages
from django.db.models import Count
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    products = Product.objects.all()
    sliders = Slider.objects.all()
    cart =Cart.objects.all().count()
    diction = {'products':products, 'cart':cart, 'sliders':sliders}
    return render(request, 'Shop/index.html', context = diction)

def wrong(request):
    diction = {}
    return render(request, 'Shop/wrong.html', context = diction)


@login_required(login_url='loginpage')
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


@login_required(login_url='loginpage')
def cart(request):
    carts = Cart.objects.all()
    total = 0
    for cart in carts:
        total = total+cart.quantity*cart.price
    cart =Cart.objects.all().count()
    diction = {'carts':carts, 'total':total, 'cart':cart}
    return render(request, 'Shop/cart.html', context = diction)

@login_required(login_url='loginpage')
def checkout(request):
    carts = Cart.objects.all()
    products = Product.objects.all()
    cartcount =carts.count()
    if(cartcount==0):
        return redirect('cart')
    if request.method=="POST":
        myform = FormCheckout(request.POST)
        user = request.user
        location = request.POST['location']
        phone = request.POST['phone']
        total = 0
        for cart in carts:
            total = total+cart.quantity*cart.price
            cartproductstock = cart.product.stock
            inspro = Product.objects.get(pk=cart.product.id)
            cartstock  = cart.quantity
            if cartstock > cartproductstock:
                messages.error(request, 'Stock not available in '+cart.product.name)
                return redirect('cart')
            else:
                newStockProduct = cart.product.stock - cart.quantity
                Product.objects.filter(pk=cart.product.id).update(stock=newStockProduct)
                
        addData = Checkout(user=request.user, location=location, phone=phone, total = total)
        addData.save()
        obj = Checkout.objects.latest('id')
        for cart in carts:
            add = Ordered(checkout=obj, product=cart.product, price=cart.price, quantity=cart.quantity)
            add.save()
        Cart.objects.filter(user=request.user).delete()
        messages.success(request, 'Checkout Done')
        return redirect('checkoutthanks')
   
    else:
        myform = FormCheckout()
    diction = {'myform':myform}
    return render(request, 'Shop/checkout.html', context = diction)



@login_required(login_url='loginpage')
def addtocart(request, id):
    if request.method=="POST":
        myform = FormCart(request.POST)
        product = Product.objects.get(pk=id)
        price = product.price
        adddata = Cart(user=request.user, product=product,price=price, quantity=1)
        adddata.save()
        messages.success(request, 'Product added to the cart')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='loginpage')
def deletethiscart(request, id):
    if request.method=="POST":
        delete_id = Cart.objects.get(pk=id)
        delete_id.delete()
        messages.success(request, 'Item Deleted')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='loginpage')
def editqtycart(request, id):
    if request.method=="POST":
        cartData = Cart.objects.get(pk=id)
        myform = FormEditQty(request.POST, instance = cartData)
        if myform.is_valid():
            quantity = myform.cleaned_data['quantity']
            if 0<quantity:
                myform.save(commit=True)
                messages.success(request, 'Qty Updated')
            else:
                messages.success(request, 'Qty Can no be Updated')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




@login_required(login_url='loginpage')
def mycheckout(request):
    checkouts = Checkout.objects.all().order_by('id')
    checkoutscount =checkouts.count()
    cart =Cart.objects.all().count()

    orders = Ordered.objects.all().order_by('id')
    diction ={'checkouts':checkouts, 'orders':orders, 'cart':cart}
    return render(request, 'Shop/mycheckout.html', context=diction)

def brands(request):
    brands = Brand.objects.all()
    cart =Cart.objects.all().count()
    diction = {'brands':brands, 'cart':cart}
    return render(request, 'Shop/brands.html', context = diction)



def brandview(request,id):
    brand = Brand.objects.get(pk=id)
    products = Product.objects.filter(brand=brand)
    cart =Cart.objects.all().count()
    diction = {'brand':brand, 'products':products, 'cart':cart}
    return render(request, 'Shop/brandview.html', context = diction)

def productview(request,id):
    product = Product.objects.get(pk=id)
    cart =Cart.objects.all().count()
    diction = {'product':product, 'cart':cart}
    return render(request, 'Shop/productview.html', context = diction)


def search(request):
    givenSearch = request.GET['search']
    results = Product.objects.filter( Q(name__icontains = givenSearch ) | Q(brand__brand__icontains = givenSearch ) | Q(code__icontains = givenSearch ) | Q(network__icontains = givenSearch ) | Q(display_details__icontains = givenSearch ) | Q(camera_details__icontains = givenSearch ) | Q(memory_details__icontains = givenSearch ) | Q(battery_details__icontains = givenSearch))
    searchCount = results.count()
    cart = Cart.objects.all().count()
    diction = { 'cart':cart, 'givenSearch':givenSearch, 'results':results, 'searchCount':searchCount}
    return render(request, 'Shop/search.html', context = diction)


@login_required(login_url='loginpage')
def checkoutthanks(request):
    cart =Cart.objects.all().count()
    diction = {'cart':cart}
    return render(request, 'Shop/checkoutthanks.html', context = diction)
