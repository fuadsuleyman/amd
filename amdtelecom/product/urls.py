from django.urls import path, include
from django.conf.urls.static import static
from .import views
from .views import (
    SearchProductListView,
    ProductsFilterListView,
    ProductDetailView,
)


app_name = 'product'

urlpatterns = [
    path('search/<str:title>/', SearchProductListView.as_view(), name='products_list_filter'),
    path('products/<slug:slug>/', ProductsFilterListView.as_view(), name='products_filter'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    # path('products/filter/<int:pk>/', views.product_detail, name='products_detail'),
    path('api/v1.0/', include('product.api.urls')),
    # path('products/', views.about, name='amd-about'),
]