from django.urls import path

from Bankapp import views

urlpatterns = [
    path('index/', views.index),
    path('registration/', views.userdb),
    path('login/', views.login),





    ]