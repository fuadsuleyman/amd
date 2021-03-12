from django.contrib import admin
from django.utils.safestring import mark_safe
from .common import slugify

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
    # Product_details_property_value,
)

admin.site.register(Product_colors)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "description", "is_main", "status", 'id')
    list_display_links = ("title",)
    readonly_fields = ('slug',)
    list_filter = ("title", "status")
    search_fields = ('title',)
    # prepopulated_fields = {'slug': ('title',)}


    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        category = form.instance
        category.slug = slugify(f'{category.parent.all().last()} {category.title}')
        category.save()


@admin.register(Marka)
class MarkaAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display = ("id", "title", "description", "slug")
    list_display_links = ("title",)

@admin.register(Product_images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image", "product")


class ImageInline(admin.TabularInline):
    model = Product_images
    extra = 0


@admin.register(Product_details_property_name)
class PropertyNameAdmin(admin.ModelAdmin):
    list_display = ("title", "status")


# @admin.register(Product_details_property_value)
# class PropertyValueAdmin(admin.ModelAdmin):
#     list_display = ("content", "file", "status")

admin.site.register(Product_details)
class ProductDetailNameAdmin(admin.TabularInline):
    model = Product_details
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "is_new", 'get_image', 'show_markas', ) #"get_image"
    list_display_links = ("title",)
    list_filter = ("price", "category",)
    search_fields = ('title', "category__title", "Marka")
    readonly_fields = ('slug',)
    inlines = [ImageInline, ProductDetailNameAdmin]
    save_on_top = True
    save_as = True #create new product easy way

    fieldsets = (
        ('Relations', {
            'fields': ('category','marka', 'tags', 'same_product'),
        }),
        ('Informations', {
            'fields': (('title', 'slug'), 'sku', 'internal_storage', 'ram', ('color_title', 'color_code',), 'operator_code', 'description', 'sale_count', ('is_featured',), 'status')
        }),
        ('Publishe', {
            'fields': ('is_published',)
        }),
        ('Kampaniya', {
            'fields': ('is_new', 'is_discount', 'discount_type', 'discount_value')
        }),
        ('Price Info', {
            'fields': ('price', 'old_price'),
        }),
    )

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        product = form.instance
        count = 0
        if not product.slug:
            # product.slug = f'{slugify(product.title)}-{product.id}'
            if product.ram and product.internal_storage:
                slug = f'{product.marka.first().title} {product.title}-{product.ram}-{product.internal_storage}-{product.color_title}'
                product.title = f'{product.marka.first().title} {product.title} {product.ram} {product.internal_storage} {product.color_title}'
                product.slug = f'{slugify(slug)}'
                
            else:
                product.title = f'{product.marka.first().title} {product.title} {product.color_title}'
        else:
            count += 1
            product.title = f'{product.marka.first().title}-{product.title}-{product.ram}-{product.internal_storage}-{product.color_title}-{product.id}-{count}'
            product.slug = f'{slugify(product.slug)}{count}'
            product.save()


    def show_markas(self, obj):
        return ' '.join([product.title for product in obj.marka.all()])

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.images.get(is_main=True).imageURL} width="50" height="60"')


    show_markas.short_description = "Marka"

    get_image.short_description = "Image"




admin.site.register(Tag)