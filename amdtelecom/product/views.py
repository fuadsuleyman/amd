from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse
from .models import (
    Product, 
    Product_images, 
    Product_details, 
    Category,
    Marka,
)
from order.models import (
    OrderItem, 
    Order,
)
from account.models import Customer



class SearchProductListView(ListView):
    model = Product
    template_name = 'search.html'
    # context_object_name = 'products'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        hide_filter = True
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, title=self.kwargs['title'])
        products = Product.objects.filter(is_published=True).filter(operator_code=None).order_by('-created_at')

        title = self.kwargs.get('title')
        if title:
            # products = Product.objects.filter(Q(category__title__icontains=title) and Q(title__icontains=title) and Q(operator_code=None))
            category = products.filter(category__title__icontains=title).filter(operator_code=None).distinct()
            product = products.filter(title__icontains=title).filter(operator_code=None).distinct()

            if category:
                products = category
            else:
                products = product
        
        return products

    def get_queryset(self):
        category = get_object_or_404(Category, title=self.kwargs['title'])
        queryset = Product.objects.filter(category=category).filter(is_published=True)
        return queryset




class ProductsFilterListView(ListView):
    model = Product
    template_name = 'products.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        products = Product.objects.filter(category=category).filter(is_published=True)
        
        # for filter template page for view or no
        marka = False
        color_title = False
        condition = False
        operator = False
        operator_data = ''

        # for news products slick slider 
        new_products = products.filter(is_published=True)

        for item in products:
            if item.marka.all():
                marka = True
                print(marka)
            if item.color_title:
                color_title = True
            if item.is_new:
                condition = True
            if item.operator_code != None:
                operator = True
            else:
                operator_data = item.operator_code
            
        # context["category"] = get_object_or_404(Category, slug=self.kwargs['slug'])
        context = {
            'products': products,
            'categories': category,
            'marka': marka,
            'color_title': color_title,
            'condition': condition,
            'operator': operator,
            'operator_data': operator_data,
            'new_products': new_products,
        }
        print(context)
        return context

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=category).filter(is_published=True)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # product = get_object_or_404(Product, id=self.kwargs['pk'])
        product = Product.objects.get(slug=self.object.slug)
        the_category = Category.objects.filter(categories = product).values_list('title', flat=True).last()
        print(the_category, 'idler')
        # categories = Category.objects.all()
        # for item in categories:
        #     item
        # related_products = Product.objects.filter(category__title__in=the_category_id).filter(is_published=True)
        related_products = Product.objects.filter(category__title=the_category).order_by('-created_at')

        # for item in category:
        #     category_id = item.id
        # print(category_id, 'kele')
        # related_products = 
        print(related_products, 'kategoriya')
        photos = Product_images.objects.filter(product=product)
        details = Product_details.objects.filter(product=product)
        context['product'] = product
        context['photos'] = photos
        context['details'] = details
        context['related_products'] = related_products
        print(details, 'sekilci')
        return context

    def post(self, request, pk):
        product = Product.objects.get(id=pk)
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()
    
