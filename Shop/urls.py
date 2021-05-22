from django.urls import path,re_path
from Shop import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('deletethiscart/<int:id>/', views.deletethiscart, name='deletethiscart'),
    path('panel/addproduct/', views.addproduct, name='addproduct'),
]
