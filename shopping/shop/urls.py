from django import views
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='shopHome'),
    path('about/',views.about,name='aboutus'),
    path('contact/',views.contact,name='contactus'),
    path('tracker/',views.tracker,name='tracker'),
    path('search/',views.search,name='search'),
    path('product/<int:myid>',views.product,name='productsearch'),
    path('checkout/',views.checkout,name='checkout'),
]
