from django.urls import path
from . import views


urlpatterns = [
    path('deletefromcart/<int:id>/', views.deletefromcart, name='deletefromcart'),
    path('cart/', views.cart, name="cart"),
]