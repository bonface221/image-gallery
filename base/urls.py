from django.urls import path 
from . import views 

urlpatterns =[
    path('', views.home, name='home'),
    path('category/<str:pk>' , views.categories, name='category'),
    path('location/<str:pk>' , views.locations, name='location'),
    path('image/<str:pk>' , views.single, name='single'),
]