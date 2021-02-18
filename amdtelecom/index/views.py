from django.shortcuts import render
from product.models import Product
from product.models import Product_details

# Create your views here.


def home_page(request):
    products = Product.objects.all()
    details = Product_details.objects.all()
    context = {'products':products, 'details': details}
    return render(request, 'home.html', context)