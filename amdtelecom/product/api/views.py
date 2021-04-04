import json
import itertools   
from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from rest_framework.response import Response

# from rest_framework.pagination import 
# from .pagination import CustomProductPaginator

from ..models import (
    Product, 
    Product_images,
    Marka,
    Category
)
from .serializers import (
    ProductSerializer, 
    ProductImageSerializer,
    ProductMarkaSerializer,
    SearchSerializer,
)


@api_view(['GET'])
def all_product(request):
    products = Product.objects.filter(is_published=True)
    serializer = ProductSerializer(products, many=True, context = {'request' : request})
    return Response(data=serializer.data, status=HTTP_200_OK)


class ProductFilterListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    # pagination_class = CustomProductPaginator

    def get_queryset(self):
        category = self.request.GET.get('category')
        products = Product.objects.filter(category=category)

        color_title = self.request.GET.getlist('color_title[]')
        internal_storages = self.request.GET.getlist('internal_storage[]')
        is_new = self.request.GET.getlist('is_new[]')
        marka = self.request.GET.getlist('marka[]')
        min_price = self.request.GET.get('price_min')
        max_price = self.request.GET.get('price_max')
        operators = self.request.GET.getlist('operator_code[]')

        if operators:
            if min_price:
                products = products.filter(operator_code__in=operators).filter(price__range=(min_price, max_price) or None)  
            else:
                products = products.filter(operator_code__in=operators or None).distinct()
        else:
            if min_price:
                products = products.filter(price__range=(min_price, max_price) or None)
        
        if color_title:
            if min_price:
                products = products.filter(color_title__in=color_title).filter(price__range=(min_price, max_price) or None)
            else:
                products = products.filter(color_title__in=color_title or None).distinct()
        else:
            if min_price:
                products = products.filter(price__range=(min_price, max_price) or None)

        if internal_storages:
            if min_price:
                products = products.filter(internal_storage__in=internal_storages).filter(price__range=(min_price, max_price) or None)
            else:
                products = products.filter(internal_storage__in=internal_storages or None).distinct()
        else:
            if min_price:
                products = products.filter(price__range=(min_price, max_price) or None)

        if is_new:
            if min_price:
                products = products.filter(is_new=is_new[0]).filter(price__range=(min_price, max_price) or None)
            else:
                products = products.filter(is_new=is_new[0] or None)
        else:
            if min_price:
                products = products.filter(price__range=(min_price, max_price) or None)

        if marka:
            if min_price:
                products = products.filter(marka__id__in=marka).filter(price__range=(min_price, max_price) or None)
            else:
                products = products.filter(marka__id__in=marka or None).distinct()
                print(products, 'markasi')
        else:
            if min_price:
                products = products.filter(price__range=(min_price, max_price) or None)        

        # try:
        #     products_images = Product_images.objects.filter()

        return products


class ProductImageListAPIView(ListAPIView):
    serializer_class = ProductImageSerializer
    queryset = Product_images.objects.all()

class ProductMarkaListAPIView(ListAPIView):
    serializer_class = ProductMarkaSerializer
    queryset = Marka.objects.all()


class SearchListAPIView(ListAPIView):
    serializer_class = SearchSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(is_published=True).filter(operator_code__isnull=False).order_by('-created_at')
        query = self.request.GET.get('q')
        if query:
            product = Product.objects.filter(operator_code=None).filter( Q(title__icontains=query) | Q(category__title__icontains=query)).order_by('-created_at').distinct()[:5]
            print(product)

        return product
