from django.urls import path,re_path
from accounts import views
urlpatterns = [
    path('/login', views.loginpage, name='loginpage'),
]
