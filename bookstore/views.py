from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Book
from .forms import ReviewForm

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
    book_type_small_network = Book.objects.filter(type_small='NET').values('title', 'link', 'author_name', 'author_link', 'pub_name', 'pub_date', 'reviews__author', 'reviews__text').annotate(Avg('reviews__grade')).order_by('-reviews__grade__avg')
    first_book = book_type_small_network[0]
    book_recommand = book_type_small_network.filter(title=first_book['title'])
    book_for_list = book_type_small_network[2::]

    return render(request, 'bookstore/computer/network.html', {
        'books' : book_type_small_network,
        'first_book' : first_book,
        'book_recommand' : book_recommand,
        'book_list' : book_for_list,
    })

def mobile(request):
    return render(request, 'bookstore/computer/mobile.html')

# 자연과학


# 경제 경영

# 역사

#리뷰 폼
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('network')
    else:
        form = ReviewForm()
    return render(request, 'bookstore/add_review.html', {'form' : form})