from django.urls import path
from . import views
# from .views import ProductListView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='amd-home'),
]