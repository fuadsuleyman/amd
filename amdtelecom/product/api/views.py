from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.shortcuts import get_object_or_404
from rest_framework.response import Response



from ..models import (
    Product, 
    Product_images,
)
from .serializers import (
    ProductSerializer, 
    ProductImageSerializer,
)


@api_view(['GET'])
def all_product(request):
    products = Product.objects.filter(is_published=True)
    serializer = ProductSerializer(products, many=True, context = {'request' : request})
    return Response(data=serializer.data, status=HTTP_200_OK)

class ProductFilterListAPIView(ListAPIView):
    serializer_class = ProductSerializer


    def get_queryset(self):
        result = True
        category = self.request.GET.get('category')

        products = Product.objects.filter(category=category)
        # products = Product.objects.filter(is_published=True)
        
        color_title = self.request.GET.getlist('color_title[]')
        is_new = self.request.GET.getlist('is_new[]')
        marka = self.request.GET.getlist('marka[]')
        min_price = self.request.GET.get('price_min')
        max_price = self.request.GET.get('price_max')

        if color_title:
            if min_price:
                products = products.filter(color_title__in=color_title).filter(price__range=(min_price, max_price) or None)
            else:
                products = products.filter(color_title__in=color_title or None).distinct()
            print(products)
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
                
        return products


class ProductImageListAPIView(ListAPIView):
    serializer_class = ProductImageSerializer
    queryset = Product_images.objects.all()