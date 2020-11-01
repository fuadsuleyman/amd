from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

# Create your views here.
from django.http import HttpResponse
from .models import Product, Product_image, Product_details


# products = [
#     {
#         'author': 'Fuad Suleymanov',
#         'title': 'Galaxy S9 Pro',
#         'description': 'So powerfull, so nice',
#         'data_posted': 'October 17, 2020'
#     },
#     {
#         'author': 'Elxan Bayramov',
#         'title': 'Galaxy S10',
#         'description': 'it is so awesome',
#         'data_posted': 'October 16, 2020'
#     },
#     {
#         'author': 'Vaqif Balayev',
#         'title': 'Apple S11',
#         'description': 'just difference',
#         'data_posted': 'October 15, 2020'
#     }

# ]
# Product.objects.all()
# def home(request):
#     context = {
#         'products': Product.objects.all()
#     }
#     return render(request, 'product/home.html', context)

# class ProductListView(ListView):
#     model = Product
#     template_name = 'product/home.html'
#     context_object_name = 'products'
#     ordering = ['-date_posted']

# bu versiya ishleyir
def home_page(request):
    products = Product.objects.all()
    details = Product_details.objects.all()
    context = {'products':products, 'details': details}
    return render(request, 'product/home.html', context)

# def home_page(request, id):
#     products = Product.objects.all()
#     prod = 
#     details = Product_details.objects.all() 
#     headphoto = Product_image.objects.first()
#     context = {'products':products, 'headphoto': headphoto, 'details': details}
#     return render(request, 'product/home.html', context)

# class ProductDetailView(DetailView):
 #     model = Product

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    photos = Product_image.objects.filter(product=product)
    details = Product_details.objects.filter(product=product)
    context = {'product':product,'photos':photos, 'details':details,}
    return render(request, 'product/product_detail.html', context)


def about(request):
    return render(request, 'product/about.html', {'title': 'About'})

