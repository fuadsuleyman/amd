from django.urls import path
from . import views
# from .views import ProductListView
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name='amd-home'),
    # path('', ProductListView.as_view(), name='amd-home'),
    path('cart/', views.cart_page, name='amd-cart'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    # path('product/<int:id>/', views.product_detail, name='product-detail'),
    # path('about/', views.about, name='amd-about'),
]