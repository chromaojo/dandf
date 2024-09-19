from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('reciept', views.reciept, name='reciept'),
    path('reciept/<str:df>', views.reciept_details, name='reciept'),
    path('register', views.register, name='register'),
    path('details/<str:df>', views.details, name='details'),
    path('customer', views.customer, name='customer'),
    path('add_to_cart/<str:df>', views.add_to_cart, name= 'add_to_cart'),
    path('cart', views.cart, name= 'cart'),
    path('checkout', views.checkout, name='checkout'),
    path('upload_Menu/<str:df>', views.upload_Menu, name ='upload_Menu'),
    path('login', views.login, name='login'),
    path('logout', views.login, name='logout'),
    path('delete_order/<str:df>', views.delete_order, name='delete_order'),
    path('delete_reciept/<str:df>', views.delete_reciept, name='delete_reciept'),
]