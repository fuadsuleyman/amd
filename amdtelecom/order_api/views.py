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
    device = request.COOKIES['device']
    print('COUNT API isheleyir')
    print('device', device)
    customer, created = Customer.objects.get_or_create(device=device)
    print('customer', customer)

    try:
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    except Order.DoesNotExist:
        order = None

    total_items = 0
    if order != None:

        for item in order.orderitem_set.all():
            print(item.quantity)
            total_items += int(item.quantity)
    else:
        total_items = 0

    return Response(total_items)

@api_view(['GET'])
def get_order_items_id(request, pk):
    device = request.COOKIES['device']
    print('ITEM_id API isheleyir')
    print('device api item_id', device)
    customer, created = Customer.objects.get_or_create(device=device)
    print('customer api item_id', customer)

    try:
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    except Order.DoesNotExist:
        order = None

    if order != None:

        # orderItems_id = order.orderitem_set.all().filter(product_id=pk).first()
        orderItems_id = order.orderitem_set.all().get(product_id=pk).id
        print('orderItems_id api item_id', orderItems_id)
        # orderItems_idserialized = seril.serialize('json', orderItems_id)
        # print('ordetItems_id from api seril', orderItems_idserialized)
        return Response(orderItems_id)



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
    print('Salam')
    serializer = OrderItemSerializer(data=request.data)
    # order_item_count = 0

    # order_item_count

    # num_results = User.objects.filter(email = cleaned_info['username']).count()

    

    if serializer.is_valid():
        print('data from create', request.data['product'])
        order1 = OrderItem.objects.filter(product_id = request.data['product']).count()
        print('SAY: ', order1)
        if order1 == 0:
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