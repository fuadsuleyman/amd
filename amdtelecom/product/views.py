from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Q
from collections import OrderedDict
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
        # print('salam')
        # category = get_object_or_404(Category, title=self.kwargs['title'])
        # products = Product.objects.filter(is_published=True).filter(operator_code=None)

        # query = self.kwargs.get('title')
        # if query:
        #     products = Product.objects.filter(operator_code=None).filter( Q(title__icontains=query) | Q(category__title__icontains=query)).order_by('-created_at').distinct()
        products = self.get_queryset
        print(products, 'datalar')
        # count = 0
        # for item in products:
        #     count += 1
        context = {
            'products': self.get_queryset,

        }

        return context

    def get_queryset(self):
        queryset = Product.objects.filter(is_published=True).filter(operator_code__isnull=False).order_by('-created_at')
        query = self.request.GET.get('q')
        # query = self.query_parametr.get()
        # query = self.kwargs['title']
        # print(query)
        if query:
            print(query, 'basliq')
            # products = Product.objects.filter(Q(category__title__icontains=title) and Q(title__icontains=title) and Q(operator_code=None))
            # category = queryset.filter(category__title__icontains=title).distinct()[:6]
            # product = queryset.filter(title__icontains=title).distinct()[:6]
            product = Product.objects.filter(operator_code=None).filter( Q(title__icontains=query) | Q(category__title__icontains=query)).order_by('-created_at').distinct()

        return product


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # product = get_object_or_404(Product, id=self.kwargs['pk'])
        product = Product.objects.get(slug=self.object.slug)
        the_category = Category.objects.filter(categories = product).values_list('title', flat=True).last()
        related_products = Product.objects.filter(category__title=the_category).order_by('-created_at')

        photos = Product_images.objects.filter(product=product)
        details = Product_details.objects.filter(product=product)
        context['product'] = product
        context['photos'] = photos
        context['details'] = details
        context['related_products'] = related_products
        print(details, 'sekilci')
        return context

    def post(self, request, **kwargs):
        slug = self.kwargs['slug']
        product = Product.objects.get(slug=slug)
        #Get user account information
        try:
            customer = self.request.user.customer	
        except:
            device = self.request.COOKIES['device']
            customer, created = Customer.objects.get_or_create(device=device)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(customer=customer, product=product, order=order)
        orderItem.quantity=request.POST['quantity']
        orderItem.save()

        return redirect('order:cart')


# def product_detail(request, slug):
#     product = Product.objects.get(slug=slug)
#     photos = Product_images.objects.filter(product=product)
#     details = Product_details.objects.filter(product=product)
#     context = {'product':product,'photos':photos,'details':details}

#     if request.method == 'POST':
#         product = Product.objects.get(slug=slug)
#         #Get user account information
#         try:
#             customer = request.user.customer	
#         except:
#             device = request.COOKIES['device']
#             customer, created = Customer.objects.get_or_create(device=device)

#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
#         orderItem.quantity=request.POST['quantity']
#         orderItem.save()

#         return redirect('order:cart')

#     return render(request, 'product_detail.html', context)

    




class ProductsFilterListView(ListView):
    model = Product
    template_name = 'products.html'


    def get_context_data(self, **kwargs):
        print('1-------', self.kwargs['slug'])
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        products = Product.objects.filter(category=category).filter(is_published=True)
        markas = Marka.objects.filter(marka__id__in=products.all()).filter(marka__isnull=False).distinct()
        # colors = products

        colors_list = products.values('color_title')
        operators_list = products.values('operator_code')
        internal_storages_list = products.values('internal_storage')
        print(internal_storages_list, 'rams list')
        print(operators_list, 'listler')
        
        # for remove duplicate color title in colors_list
        colors = []
        [colors.append(i['color_title']) for i in colors_list if i['color_title'] not in colors]
        # remove duplicate operator code in list
        operators_codes = []
        [operators_codes.append(i['operator_code']) for i in operators_list if i['operator_code'] not in operators_codes]
        print(operators_codes, 'kodlar')

        # for append list only defaul not none ram field no duplicate
        internal_storages = []
        # [internal_storages.append(i['internal_storage']) for i in internal_storages_list if i['internal_storage'] not in internal_storages]

        for i in internal_storages_list:
            if i['internal_storage'] != None:
                internal_storages.append(i['internal_storage'])
        internal_storages = list(dict.fromkeys(internal_storages))


        # for filter template page for view or no
        marka = False
        color_title = False
        internal_storage = False
        condition = False
        operator = False
        operator_data = ''

        # for news products slick slider 
        new_products = products.filter(is_published=True).order_by('-created_at')[:3]

        for item in products:
            if item.marka.all():
                marka = True
            if item.color_title:
                color_title = True
            if item.internal_storage:
                internal_storage = True
            if item.is_new:
                condition = True
            if item.operator_code != None:
                operator = True
            else:
                operator_data = item.operator_code
            
        context = {
            'products': products,
            'categories': category,
            'marka': marka,
            'markas': markas,
            'color_title': color_title,
            'internal_storage': internal_storage,
            'internal_storages': internal_storages,
            'colors': colors,
            'condition': condition,
            'operator': operator,
            'operator_data': operator_data,
            'operators_codes': operators_codes,
            'new_products': new_products,
        }
        print(context)
        return context

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        queryset = Product.objects.filter(category=category).filter(is_published=True)
        return queryset


# def product_filter(request, slug):
#     print(slug, 'belede')
#     category = Category.objects.get(slug=slug)
#     print(category, 'belede')
#     products = Product.objects.filter(category=category).first()
#     print(products, 'elcn')
#     context = {
#         'products_list': products,
#         'categories': category
#     }
#     return render(request, 'products.html', context)
