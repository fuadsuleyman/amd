from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView

# Create your views here.
from django.http import HttpResponse
from .models import Product, Product_images, Product_details
from order.models import OrderItem, Order
from account.models import Customer



class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-created_at']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def product_detail(request, id):
    product = Product.objects.get(id=id)
    photos = Product_images.objects.filter(product=product)
    details = Product_details.objects.filter(product=product)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('cart')
    context = {'product':product,'photos':photos, 'details':details,}
    return render(request, 'product_detail.html', context)

# class ProducDetailView(DetailView):
#     model = Product
#     template_name = "product.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context[""] = 
#         return context
    