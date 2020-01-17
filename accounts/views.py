from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'], password = request.POST["password1"])
            auth.login(request, user)
            return redirect('bookstore/homepage')
        return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bookstore/homepage')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('bookstore/homepage')


def facebook(request):
    return render(request, 'accounts/facebook.html')

def github(request):
    return render(request, 'accounts/github')

def google(request):
    return render(request, 'accounts/google.html')
