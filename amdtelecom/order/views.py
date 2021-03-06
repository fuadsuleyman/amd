from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.contrib.messages import success
# Create your views here.

from account.models import Customer

from .models import OrderItem, Order
from .forms import CheckoutForm

# def cart(request):
#     device = request.COOKIES['device']
#     customer, created = Customer.objects.get_or_create(device=device)

#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#     context = {'order':order}
#     return render(request, 'cart.html', context)

def deletefromcart(request, id):
    cartitem = OrderItem.objects.get(id=id)
    cartitem.delete()
    return redirect('cart')

def cart(request):
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    imgs = {}
    for item in items:
        print('cart-item:', item)
        print('cart-item.product:', item.product)
        imgs.update({item.id: item.product.images.get(is_main=True).imageURL})
    context = {'order':order, 'imgs': imgs}
    return render(request, 'cart.html', context)

class CheckoutView(CreateView):
    form_class = CheckoutForm
    template_name = 'checkout.html'
    def form_valid(self, form):
        success(self.request, 'Sifarisiniz qeyde alinmisdir tez bir zamanda sizinle elaqe saxlanilicaq.')
        # success_url = reverse_lazy('index:home')
        return redirect('index:home')
