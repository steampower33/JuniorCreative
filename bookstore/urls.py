from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('computer/', views.computer, name = 'computer'),
    path('computer/game/', views.game, name='game'),
    path('computer/graphic/', views.graphic, name='graphic'),
    path('computer/network/', views.network, name = 'network'),
    path('computer/mobile/', views.mobile, name='mobile'),
    path('add_review/', views.add_review, name='add_review'),
]
