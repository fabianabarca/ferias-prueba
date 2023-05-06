from django.urls import path
from .views import index
from .views import acerca
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('acerca/', views.acerca, name='acerca'),
]