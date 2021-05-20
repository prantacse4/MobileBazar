from django.urls import path,re_path
from Shop import views
urlpatterns = [
    path('', views.index, name='index'),
]
