from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
# Create your views here.

from account.models import Customer

from .models import OrderItem, Order
from .forms import CheckoutForm

def cart(request):
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    context = {'order':order}
    return render(request, 'cart.html', context)

def deletefromcart(request, id):
    cartitem = OrderItem.objects.get(id=id)
    cartitem.delete()
    return redirect('cart')


class ContactCreateView(CreateView):
    form_class = CheckoutForm
    template_name = 'contact.html'
    success_url = reverse_lazy('index:home')
