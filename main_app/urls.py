from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about),
     path('superheroes/', views.superheroes_index, name='index'),
]