from django.shortcuts import render

# Create your views here.

from .models import Cart

def cart_page(request):
    cart = Cart.objects.all()[0]
    context = {'cart':cart}
    return render(request, 'cart/cart.html', context)