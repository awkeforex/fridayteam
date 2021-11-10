from django.urls import path
from django.views.generic.base import TemplateView
from . import  views
from  django.contrib.auth import views as auth_views


urlpatterns = [
    path("login/", views.loginpage , name='login'),
    path("logout/", views.logoutpage , name='logout'),
    path("register/", views.registerpage , name='register'),

    path("reset_password/",auth_views.PasswordResetView.as_view(
        template_name = 'members/password_reset.html'
    ) , name='password_reset'),
    path("reset_password_sent/",auth_views.PasswordResetDoneView.as_view(
        template_name='members/password_reset_sent.html'
    ) , name='password_reset_done'),
    path("reset/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(
        template_name = 'members/password_reset_confirm.html'
    ) , name='password_reset_confirm'),
    path("reset_password_complete/",auth_views.PasswordResetCompleteView.as_view(
        template_name = "members/password_reset_complete.html") 
        , name='password_reset_complete'),


    path('update-user/', views.updateUser , name='update-user'),


  
    

   
]
