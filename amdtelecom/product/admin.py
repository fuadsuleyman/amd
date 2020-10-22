from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Category, Product_image, Product_details

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product_image)
admin.site.register(Product_details)