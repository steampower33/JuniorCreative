from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('computer/', views.computer, name = 'computer'),
    path('computer/network/', views.network, name = 'network'),
]