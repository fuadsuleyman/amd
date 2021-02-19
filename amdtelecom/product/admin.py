from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import (
    Product, 
    Marka, 
    Category, 
    Product_details, 
    Product_colors, 
    Product_images,
    Tag,
    Product_details_property,
    Product_details_property_name,
)

admin.site.register(Product_colors)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = ("title",)
    readonly_fields = (
        'slug',
    )

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ("id", "device")
#     list_display_links = ("device",)

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("id", "date_ordered")
#     list_display_links = ("date_ordered",)

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ("id", "quantity", "date_added")
#     list_display_links = ("quantity",)

@admin.register(Marka)
class MarkaAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = ("title",)
    readonly_fields = ('slug',)

# @admin.register(Product_colors)
# class ColorpAdmin(admin.ModelAdmin):
#     list_display = ("id", "color_name", "color_code")
#     list_display_links = ("color_name",)

class ImageInline(admin.TabularInline):
    model = Product_images
    extra = 0
class ImageInline(admin.TabularInline):
    model = Product_images
    extra = 0

# class DetailsInline(admin.t):
#     model = Product_details
#     extra = 0

class DetailsInline(admin.TabularInline):
    '''Tabular Inline View for '''

    model = Product_details
    # min_num = 3
    # max_num = 20
    # extra = 1
    # raw_id_fields = (,)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price") #"get_image"
    list_display_links = ("title",)
    list_filter = ("price",)
    search_fields = ('title', "category__name")
    inlines = [ImageInline, DetailsInline]
    save_on_top = True
    save_as = True #create new product easy way

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    # get_image.short_description = "Image"
    # get_image.allow_tags = True


admin.site.register(Tag)
admin.site.register(Product_images)
admin.site.register([Product_details, Product_details_property, Product_details_property_name])