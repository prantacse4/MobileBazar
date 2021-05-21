from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from .models import *
from .forms import FormProduct
from django.db.models import Q
from django.shortcuts import redirect
from  django.contrib import messages
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    diction = {}
    return render(request, 'Shop/index.html')

def wrong(request):
    diction = {}
    return render(request, 'Shop/wrong.html')

def addproduct(request):
    brand = Brand.objects.all()
    myform = FormProduct()
    if request.method=="POST":
        myform = FormProduct(request.POST, request.FILES)
        if myform.is_valid():
            myform.save(commit=True)
            messages.success(request, 'Your profile was updated.')
        
    diction = {'myform':myform, 'brand':brand}
    return render(request, 'Shop/panel/addproduct.html', context = diction)