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
    books = Book.objects.filter(type_of_book='COM').values('title', 'reviews__text', 'reviews__author', 'reviews__grade').annotate(Avg('reviews__grade')).order_by('-reviews__grade__avg')
    book_for_title = books[0]
    final_books = books.filter(title=book_for_title['title'])
    return render(request, 'bookstore/computer/game.html', {
        'books' : books,
        'book_for_title' : book_for_title,
        'final_books' : final_books
    })

def graphic(request):
    return render(request, 'bookstore/computer/graphic.html')

def network(request):
    return render(request, 'bookstore/computer/network.html')

def mobile(request):
    return render(request, 'bookstore/computer/mobile.html')

# 자연과학


# 경제 경영

# 역사
