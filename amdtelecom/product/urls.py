from django.urls import path, include
from . import views
from .views import ProductListView
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    # path('', views.home, name='amd-home'),
    path('products/', ProductListView.as_view(), name='prodducts_detail'),
    # path('', views.home_page, name='amd-home'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:id>/', views.product_detail, name='products_detail'),
    # path('products/', views.about, name='amd-about'),
    path('api/v1.0/', include('product.api.urls')),
]