from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Order, OrderItem, Checkout

# admin.site.register(Order)
# admin.site.register(OrderItem)
admin.site.register(Checkout)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "transaction_id", "complete",)
    list_display_links = ("created_at",)
    list_filter = ("complete",)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "quantity", "created_at")
    list_display_links = ("quantity",)
    list_filter = ("quantity", "product__title",)
    search_fields = ('product__title',)

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.product.images.get(is_main=True).imageURL} width="50" height="60"')

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.images.get(is_main=True).imageURL} width="50" height="60"')    
    
    # get_image.short_description = "Image"