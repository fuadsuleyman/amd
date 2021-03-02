from django.urls import path, include
from .import views
from .views import (
    ProductsFilterListView,
    ProductDetailView
)
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    path('products/<slug:slug>/', ProductsFilterListView.as_view(), name='products_filter'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    # path('products/filter/<int:pk>/', views.product_detail, name='products_detail'),
    path('api/v1.0/', include('product.api.urls')),
]