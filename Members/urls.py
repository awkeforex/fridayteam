from django.urls import path
from . import  views


urlpatterns = [
    path("login/", views.loginpage , name='login'),
    path("logout/", views.logoutpage , name='logout'),
    path("register/", views.registerpage , name='register'),


    path('update-user/', views.updateUser , name='update-user'),
  
    

   
]
