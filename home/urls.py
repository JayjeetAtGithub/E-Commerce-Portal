from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('books/<int:booktype>',views.books,name='books'),
    path('add/<int:bookid>',views.add,name='add'),
    path('cart/',views.cart,name='cart'),
    path('remove/<int:un_book_id>',views.remove,name='remove'),
    path('confirmation/',views.confirmation,name='confirmation')

]
