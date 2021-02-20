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
    Product_details_property_name,
    Product_details_property_value,
)

admin.site.register(Product_colors)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = ("title",)
    readonly_fields = (
        'slug',
    )


@admin.register(Marka)
class MarkaAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = ("title",)

# @admin.register(Product_colors)
# class ColorpAdmin(admin.ModelAdmin):
#     list_display = ("id", "color_name", "color_code")
#     list_display_links = ("color_name",)

class ImageInline(admin.TabularInline):
    model = Product_images
    extra = 0
    
@admin.register(Product_details_property_name)
class DetailAdmin(admin.ModelAdmin):
    list_display = ("title", "status")

@admin.register(Product_details_property_value)
class DetailAdmin(admin.ModelAdmin):
    list_display = ("title", "status")


class ProductDetailNameAdmin(admin.TabularInline):
    model = Product_details
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_new",) #"get_image"
    list_display_links = ("title",)
    list_filter = ("price", "category",)
    search_fields = ('title', "category__title", "Marka")
    inlines = [ImageInline, ProductDetailNameAdmin]
    save_on_top = True
    save_as = True #create new product easy way

    fieldsets = (
        ('Relations', {
            'fields': ('category','marka', 'tags', 'same_product'),
        }),
        ('Informations', {
            'fields': (('title', 'slug'), 'sku', ('color_title', 'color_code',), 'description', 'sale_count', ('is_new', 'is_featured', 'is_discount'), 'status')
        }),
        ('Price Info', {
            'fields': ('price', 'discount_type', 'discount_value'),
        }),
    )

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.images.get(is_main=True).imageURL} width="50" height="60"')


    # get_image.short_description = "Image"
    

admin.site.register(Tag)
admin.site.register([Product_images, ])