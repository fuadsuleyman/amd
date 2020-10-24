from django.contrib import admin

# Register your models here.
from .models import Product, Brand, Category, Product_image, Product_details

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("name",)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    list_display_links = ("name",)

class ImageInline(admin.TabularInline):
    model = Product_image
    extra = 0

class DetailsInline(admin.StackedInline):
    model = Product_details
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category","brand", "price") #"get_image"
    list_display_links = ("title",)
    list_filter = ("brand", "price", "category")
    search_fields = ('title', "category__name", "brand__name")
    inlines = [ImageInline, DetailsInline]
    save_on_top = True
    save_as = True #create new product easy way

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    # get_image.short_description = "Shekil"


# admin.site.register(Product)
# admin.site.register(Brand)
# admin.site.register(Category, CategoryAdmin)
admin.site.register(Product_image)
admin.site.register(Product_details)