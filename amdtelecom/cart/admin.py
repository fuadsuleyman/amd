from django.contrib import admin

from .models import Cart
# Register your models here.

# bu asagidaki ashibka verdi
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ("id", "products", "total")
#     list_display_links = ("products",)

class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

admin.site.register(Cart, CartAdmin)