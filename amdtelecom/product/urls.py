from django.urls import path, include
from django.conf.urls.static import static
from .import views
from .views import (
    SearchProductListView,
    ProductsFilterListView,
    # product_filter
    product_detail,
    # ProductDetailView
)


app_name = 'product'

urlpatterns = [
    path('search/<str:title>/', SearchProductListView.as_view(), name='products_list_filter'),
    path('products/<slug:slug>/', ProductsFilterListView.as_view(), name='products_filter'),
    # path('products/<slug:slug>/', product_filter, name='products_filter'),
    # path('', views.home_page, name='amd-home'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    # path('products/filter/<int:pk>/', views.product_detail, name='products_detail'),
    path('api/v1.0/', include('product.api.urls')),
    # path('products/', views.about, name='amd-about'),
]