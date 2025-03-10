# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('',views.sadik,name='home'),
    path('shop',views.shop,name='shop'),
    path('category',views.category,name='category'),
    path('about',views.about,name='about'),
]
