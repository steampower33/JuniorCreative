from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('facebook/', views.facebook, name='facebook'),
    path('github/', views.github, name='github'),
    path('google/', views.google, name='google'),
]