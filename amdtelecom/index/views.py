import datetime
from django.conf import settings
from product.models import Product
from order.models import Order
from account.models import Customer
from product.models import Product_details, Category
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


# def home_page(request):
#     products = Product.objects.all()
#     category = Category.objects.all()
#     details = Product_details.objects.all()
#     context = {'products':products, 'details': details,'category':category }
#     return render(request, 'home.html', context)


# class HomePageTemplateView(TemplateView):
#     template_name = 'home.html'
    # def get(self, *args, **kwargs):
    #     key='device'
    #     value = uuid.uuid4().hex
    #     days_expire=7
    #     if days_expire is None:
    #         max_age = 365 * 24 * 60 * 60  # one year
    #     else:
    #         max_age = days_expire * 24 * 60 * 60
    #         expires = datetime.datetime.strftime(
    #             datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
    #             '%a, %d-%b-%Y %H:%M:%S GMT'
    #         )

    #     response = HttpResponse()
    #     print(response, 'assas')
        
    #     response.set_cookie(
    #         key=key,
    #         value=json.dumps(value),
    #         max_age=max_age,
    #         expires=expires,
    #         # domain=settings.SESSION_COOKIE_DOMAIN,
    #         secure=settings.SESSION_COOKIE_SECURE or None
    #     )   
    #     return response
        
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # self.set_cookiee()
    #     response = HttpResponse()
    #     response.set_cookie("cookie_name", "cookie_value")
    #     response.write(template.render(context))
    #     # if self.request.COOKIES['device']:
    #     device = self.request.COOKIES['device']
    #     customer, created = Customer.objects.get_or_create(device=device)
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     products = Product.objects.all()
    #     category = Category.objects.all()
    #     details = Product_details.objects.all()
    #     # for home page return filter products
    #     new_arrivals = products.filter(is_published=True).filter(is_new=True).order_by('-created_at')[:12]
    #     most_sold = products.filter(is_published=True).order_by('-sale_count')[:12]
    #     discounted_products = products.filter(is_published=True).filter(is_discount=True).order_by('-created_at')[:12]

    #     context = {
    #         'products':products, 
    #         'details': details,
    #         'category':category, 
    #         'customer': customer, 
    #         'order': order, 
    #         'new_arrivals': new_arrivals, 
    #         'discounted_products': discounted_products, 
    #         'most_sold': most_sold,
    #         # 'response': response
    #     }
        
    #     return context



# def set_cookie(response, key, value, days_expire=7):
#     if days_expire is None:
#         max_age = 365 * 24 * 60 * 60  # one year
#     else:
#         max_age = days_expire * 24 * 60 * 60
#     expires = datetime.datetime.strftime(
#         datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
#         "%a, %d-%b-%Y %H:%M:%S GMT",
#     )
#     response.set_cookie(
#         key,
#         value,
#         max_age=max_age,
#         expires=expires,
#         domain=settings.SESSION_COOKIE_DOMAIN,
#         secure=settings.SESSION_COOKIE_SECURE or None,
#     )

def home_page(request):
    print("sasas")
    # response = HttpResponse("congrulate you device cookie created")
    # set_cookie(response, 'name', 'jujule')
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    products = Product.objects.all()
    category = Category.objects.all()
    details = Product_details.objects.all()
    # for home page return filter products
    new_arrivals = products.filter(is_published=True).filter(is_new=True).order_by('-created_at')[:12]
    most_sold = products.filter(is_published=True).order_by('-sale_count')[:12]
    discounted_products = products.filter(is_published=True).filter(is_discount=True).order_by('-created_at')[:12]

    context = {
        'products':products, 
        'details': details,
        'category':category, 
        'customer': customer, 
        'order': order, 
        'new_arrivals': new_arrivals, 
        'discounted_products': discounted_products, 
        'most_sold': most_sold,
    }
    
    return render(request, 'home.html', context)

def autocomplete(request):
    print(request.Get.get("term"))
    if 'term' in request.GET:
        qs = Product.objects.filter(title__icontains=request.GET.get('term'))
        titles = list()
        for product in qs:
            titles.append(product.title)
        # titles = [product.title for product in qs]
        return JsonResponse(titles, safe=False)
    return render(request, 'core/home.html')