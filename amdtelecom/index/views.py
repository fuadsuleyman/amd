from order.models import Order
from account.models import Customer
from product.models import Product
from product.models import Product_details, Category
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def home_page(request):
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    products = Product.objects.all()
    category = Category.objects.all()
    details = Product_details.objects.all()
    context = {'products':products, 'details': details,'category':category, 'customer': customer, 'order': order}
    return render(request, 'home.html', context)


# class HomePageTemplateView(TemplateView):
#     template_name = 'home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         products = Product.objects.all()
#         category = Category.objects.all()
#         details = Product_details.objects.all()
#         context["products"] = products
#         context["details"] = details
#         context["category"] = category
#         return context
    

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