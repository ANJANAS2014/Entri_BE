from django.urls import path

from . import views

urlpatterns = [
    path('listUsers', views.listUsers, name='listUsers'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('availabletime', views.availabletime, name='availabletime'),
]
