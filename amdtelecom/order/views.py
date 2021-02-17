from django.shortcuts import render, redirect

# Create your views here.

from account.models import Customer

from .models import OrderItem, Order

def cart(request):
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {'order':order}
    return render(request, 'order/cart.html', context)

def deletefromcart(request, id):
    cartitem = OrderItem.objects.get(id=id)
    cartitem.delete()
    return redirect('cart')