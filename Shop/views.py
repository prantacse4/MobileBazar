from django.shortcuts import render

# Create your views here.


def index(request):
    diction = {}
    return render(request, 'Shop/index.html')

def wrong(request):
    diction = {}
    return render(request, 'Shop/wrong.html')