from django.shortcuts import render
from django.db.models import Avg
from .models import Book

# Create your views here.
def homepage(request):
    return render(request, 'bookstore/homepage.html')

# 컴퓨터
def computer(request):
    return render(request, 'bookstore/computer/computer.html')

def game(request):
    return render(request, 'bookstore/computer/game.html', {
    })

def graphic(request):
    return render(request, 'bookstore/computer/graphic.html')

def network(request):
    return render(request, 'bookstore/computer/network.html', {

    })

def mobile(request):
    return render(request, 'bookstore/computer/mobile.html')

# 자연과학


# 경제 경영

# 역사
