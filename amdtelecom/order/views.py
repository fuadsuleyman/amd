from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls.base import reverse_lazy
from django.contrib.messages import success, error
# Create your views here.

from account.models import Customer

from .models import OrderItem, Order
from .forms import CheckoutForm
from .signals import send_form

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

    items = OrderItem.objects.filter(customer=customer)
    
    imgs = {}
    total=0
    for item in items:
        imgs.update({item.id: item.product.images.get(is_main=True).imageURL})
        total += item.get_total
    context = {
        'items':items,
        'imgs':imgs,
        'total':total
        }
    return render(request, 'cart.html', context)

class CheckoutView(CreateView):
    form_class = CheckoutForm
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        device = self.request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        items = OrderItem.objects.filter(customer=customer)
        total=0
        for item in items:
            total += item.get_total
        context = {'items': items, 'form': CheckoutForm, 'total':total}
        return context
    
    def form_valid(self, form):
        success(self.request, 'Sifarisiniz qeyde alinmisdir tez bir zamanda sizinle elaqe saxlanilicaq.')
        device = self.request.COOKIES['device']
        customer = Customer.objects.get(device=device)
        obj = form.save(commit=False)
        obj.customer=customer
        items = OrderItem.objects.filter(customer=customer)


        obj.complete = True
        obj.save()
        obj.orderitem_set.set(items)
        send_form(instance=obj)
        # success_url = reverse_lazy('index:home')
        # form.save()
        return redirect('index:home')

# def checkout(request):
#     device = request.COOKIES['device']
#     customer, created = Customer.objects.get_or_create(device=device)
#     order, created = Order.objects.get_or_create(customer=customer, complete=False)
#     items = order.orderitem_set.all()
#     total = 0
#     for item in items:
#         total += item.get_total
#     context = {'order':order, 'form': CheckoutForm, 'total': total}

#     if request.method == 'POST':
#         form = CheckoutForm(request.POST)
#         if form.is_valid():
#             order.complete = True
#             success(request, 'Sifarisiniz qeyde alinmisdir tez bir zamanda sizinle elaqe saxlanilicaq.')
#             return redirect('index:home')
#     return render(request, 'checkout.html', context)
