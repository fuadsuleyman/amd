from django.urls import path

from .views import ProductFilterListAPIView


app_name = 'product_apis'



urlpatterns = [
    path('filter-api-product/<int:id>/', ProductFilterListAPIView.as_view(), name='api_filter_product'),
]

