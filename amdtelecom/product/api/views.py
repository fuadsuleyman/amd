from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404

from ..models import Product
from .serializers import ProductSerializer



class ProductFilterListAPIView(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        # context = super().get_queryset()
        print('desa')
        # product = get_object_or_404(Product, id=self.kwargs['id'])
        product = Product.objects.filter(id=self.kwargs['id'])
        if product:
            return product  
        return "Product not founded"

        print(product, 'beledes')


        