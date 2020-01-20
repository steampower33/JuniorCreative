from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Book
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'bookstore/homepage.html')


def newhome(request):
    return render(request, 'bookstore/newhome.html')

# 컴퓨터
def computer(request):
    return render(request, 'bookstore/computer/computer.html')


@login_required
def game(request):
    return render(request, 'bookstore/computer/game.html', {
    })

@login_required
def graphic(request):
    return render(request, 'bookstore/computer/graphic.html')

@login_required
def network(request):
    book_type_small_network = Book.objects.filter(type_small='NET').values('title', 'link', 'author_name', 'author_link', 'pub_name', 'pub_date', 'reviews__author', 'reviews__text', 'reviews__grade', 'pk').annotate(Avg('reviews__grade')).order_by('-reviews__grade__avg')
    book_for_aver = Book.objects.filter(type_small='NET').values('title').annotate(Avg('reviews__grade')).order_by('-reviews__grade__avg')
    book_aver = book_for_aver[0]
    first_book = book_type_small_network[0]
    book_recommand = book_type_small_network.filter(title=first_book['title'])
    count = book_recommand.count()
    book_for_list = book_type_small_network[count::]

    book = get_object_or_404(Book, pk = first_book['pk'])
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            
            return redirect('network')
    else:
        form = ReviewForm()

    return render(request, 'bookstore/computer/network.html', {
        'books' : book_type_small_network,
        'first_book' : first_book,
        'book_recommand' : book_recommand,
        'book_list' : book_for_list,
        'book_aver' : book_aver,
        'form' : form,
    })


@login_required
def mobile(request):
    return render(request, 'bookstore/computer/mobile.html')

# 자연과학


# 경제 경영

# 역사

#리뷰 폼

