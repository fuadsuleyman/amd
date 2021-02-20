from django.urls import path, include
from .import views
from .views import (
    ProductListView, 
    CategoryListView,
    ProductsFilterListView,
    # product_filter
)
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    path('', CategoryListView.as_view(), name='amd-home'),
    path('products/', ProductListView.as_view(), name='products_detail'),
    path('products/<slug:slug>/', ProductsFilterListView.as_view(), name='products_filter'),
    # path('products/<slug:slug>/', product_filter, name='products_filter'),
    # path('', views.home_page, name='amd-home'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    # path('product/<int:id>/', views.product_detail, name='products_detail'),
    # path('products/', views.about, name='amd-about'),
    path('api/v1.0/', include('product.api.urls')),
]