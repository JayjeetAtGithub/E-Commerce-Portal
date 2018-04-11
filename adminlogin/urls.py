from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.admin,name='admin'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='adminlogout')
]