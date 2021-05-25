from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from .models import Profile
from django.db.models import Q
from django.shortcuts import redirect
from  django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Count
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import  ProfileForm, UserCreationForm
from Shop.models import *


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginpage(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            enteremail = User.objects.filter(username = username).count()
            if enteremail > 0:
                enteremail = User.objects.filter(email = username).count()
                if enteremail > 0:
                    enteremail = True
                else:
                    enteremail = False
            else:
                enteremail = False

            try:
                user = authenticate(request, username=User.objects.get(email=username), password=password)
                
            except:
                user = authenticate(request, username=username, password=password)

            if user is not None:
                if enteremail == True:
                    is_what = User.objects.get(email=username)
                else:
                    is_what = User.objects.get(username=username)

                is_superuser = is_what.is_superuser
                login(request, user)
                if is_superuser == True:
                    return HttpResponseRedirect('/admin')
                    
                return redirect('index')
            
            else:
                messages.info(request, 'Incorrect Username or Password')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        
    diction = {}
    return render(request, 'Shop/login.html')


def signuppage(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        myform = UserCreationForm()
        if request.method == 'POST':
            myform = UserCreationForm(request.POST)
            if myform.is_valid():
                myform.save(commit=True)
                user = myform.cleaned_data.get('username')
                messages.success(request, 'Account Created'+ user)
                return redirect('loginpage')

        diction = {'myform':myform}
        return render(request, 'Shop/signup.html', context = diction)


@login_required(login_url='loginpage')
def profile(request):
    diction = {}
    return render(request, 'Shop/profile.html', context = diction)

@login_required(login_url='loginpage')
def updateprofile(request):
    user = request.user
    myprofile = Profile.objects.get(pk=user)
    diction = {'myprofile':myprofile}
    return render(request, 'Shop/updateprofile.html', context = diction)


@login_required(login_url='loginpage')
def updateprofiledetails(request):
    user = request.user
    check = Profile.objects.filter(user=user)
    if check:
        ins = Profile.objects.get(pk=user)
        if request.method=="POST":
            myform = ProfileForm(request.POST, request.FILES, instance=ins)
            if myform.is_valid():
                myform.save(commit=True)
                messages.success(request, 'Profile Updated')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            else:
                diction = {'myform':myform}
                return render(request, 'Shop/updateprofile.html', context = diction)

    else:
        if request.method=="POST":
            myform = ProfileForm(request.POST, request.FILES,)
            if myform.is_valid():
                myform.save(commit=True)
                messages.success(request, 'Profile Details Created')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                diction = {'myform':myform}
                return render(request, 'Shop/updateprofile.html', context = diction)

@login_required(login_url='loginpage')
def logoutuser(request):
    logout(request)
    return redirect('index')


@login_required(login_url='loginpage')
def delete_my_account(request):
    if request.method == 'POST':
        userdata = request.user.id
        del_id = User.objects.get(id=userdata)
        profile = Profile.objects.filter(user=request.user)
        Cart.objects.filter(user=request.user).delete()
        checkouts = Checkout.objects.filter(user=request.user)
        Ordered.objects.filter(checkout=checkouts).delete()
        Checkout.objects.filter(user=request.user).delete()
        profile.delete()
        del_id.delete()
        logout(request)
        return redirect('index')


