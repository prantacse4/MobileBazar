from django.urls import path,re_path
from Shop import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('addtocart/<int:id>/', views.addtocart, name='addtocart'),
    path('editqtycart/<int:id>/', views.editqtycart, name='editqtycart'),
    path('deletethiscart/<int:id>/', views.deletethiscart, name='deletethiscart'),
    path('panel/addproduct/', views.addproduct, name='addproduct'),
]
