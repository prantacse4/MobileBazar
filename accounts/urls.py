from django.urls import path,re_path
from accounts import views
urlpatterns = [
    path('login/', views.loginpage, name='loginpage'),
    path('signup/', views.signuppage, name='signuppage'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('updateprofiledetails/', views.updateprofiledetails, name='updateprofiledetails'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('delete_my_account/', views.delete_my_account, name='delete_my_account'),


]
