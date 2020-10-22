from django.urls import path
from . import views
from .views import ProductListView, ProductDetailView

urlpatterns = [
    # path('', views.home, name='amd-home'),
    path('', ProductListView.as_view(), name='amd-home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('about/', views.about, name='amd-about'),
]