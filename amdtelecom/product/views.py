from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Product


products = [
    {
        'author': 'Fuad Suleymanov',
        'title': 'Galaxy S9 Pro',
        'description': 'So powerfull, so nice',
        'data_posted': 'October 17, 2020'
    },
    {
        'author': 'Elxan Bayramov',
        'title': 'Galaxy S10',
        'description': 'it is so awesome',
        'data_posted': 'October 16, 2020'
    },
    {
        'author': 'Vaqif Balayev',
        'title': 'Apple S11',
        'description': 'just difference',
        'data_posted': 'October 15, 2020'
    }

]
# Product.objects.all()
def home(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'product/home.html', context)

def about(request):
    return render(request, 'product/about.html', {'title': 'About'})