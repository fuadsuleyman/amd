from django.http.response import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from account.models import Customer

# Create your views here.

# all_products, get_product, create_product, update_product, delete_product

from order.models import Order, OrderItem

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from .serializers import OrderItemSerializer
# from .serializers import ProductPriceUpdateSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'All OrderItems':'/order-item-list/',
        'Detail View':'/order-item-detail/<str:pk>/',
        'Create':'/order-item-create/',
        'Update':'/order-item-update/<str:pk>/',
        'Patch':'/order-item-patch/<str:pk>/',
        'Delete':'/order-item-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def all_order_items(request):
    orderItems = OrderItem.objects.all()
    serializer = OrderItemSerializer(orderItems, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_order_items_count(request):
    # orderItems = OrderItem.objects.all()
    # serializer = OrderItemSerializer(orderItems, many=True)
    # count = OrderItem.objects.count()
    device = request.COOKIES['device']
    customer, created = Customer.objects.get_or_create(device=device)
    order = Order.objects.get_or_create(customer=customer, complete=False)

    try:
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    except Order.DoesNotExist:
        order = None

    total_items = 0
    if order:
        # items_count = order.orderitem_set.all().count()
        for item in order.orderitem_set.all():
            print(item.quantity)
            total_items += int(item.quantity) 
    else:
        total_items = 0

    return Response(total_items)



@api_view(['GET'])
def get_order_item(request, pk):
    try:
        orderItem = OrderItem.objects.get(id=pk)
        serializer = OrderItemSerializer(orderItem, many=False)
    except OrderItem.DoesNotExist:
        raise Http404
    return Response(serializer.data)




@api_view(['POST'])
def create_order_item(request):
    serializer = OrderItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PATCH'])
def patch_order_item(request, pk):
    try:
        orderItem = OrderItem.objects.get(id=pk)
        serializer = OrderItemSerializer(instance=orderItem, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # orderItem.get_total()
    except OrderItem.DoesNotExist:
        raise Http404
    
    return Response(serializer.data)

@api_view(['PUT'])
def update_order_item(request, pk):
    try:
        orderItem = OrderItem.objects.get(id=pk)
        serializer = OrderItemSerializer(instance=orderItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except OrderItem.DoesNotExist:
        raise Http404
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_order_item(request, pk):
    try:
        orderItem = OrderItem.objects.get(id=pk)
        orderItem.delete()
        orderItem.get_total
    except OrderItem.DoesNotExist:
        raise Http404
    return Response('Item successfully deleted!')

class ApiOrderItemsView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    pagination_class = PageNumberPagination