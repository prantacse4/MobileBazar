from django.shortcuts import render

# Create your views here.

def loginpage(request):
    diction = {}
    return render(request, 'accounts/login.html')