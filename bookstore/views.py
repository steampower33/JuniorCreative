from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'bookstore/homepage.html')

def computer(request):
    return render(request, 'bookstore/computer.html')

def network(request):
    return render(request, 'bookstore/network.html')