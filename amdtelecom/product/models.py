from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import template

register = template.Library()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f'{self.name}'

class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f'{self.name}'

class Color_p(models.Model):
    color_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    color_code = models.CharField(max_length=50, blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.color_name}'

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    sku = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=1)
    price_old = models.DecimalField(max_digits=7, decimal_places=2, default=1)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    internal_storage = models.CharField(max_length=50, blank=True, null=True, default=None)
    ram = models.CharField(max_length=50, blank=True, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color_pro = models.ForeignKey(Color_p, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.title}, {self.description}'
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    # @property
    # def sorted_image_set(self):
    #     return self.images.last().image

    # def get_last_image(self):
    #     try:
    #         last_image = self.images.last().image
    #     except AttributeError:
    #         last_image = self.image

class Customer(models.Model):
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'name: {self.device}'

class Product_image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'{self.product.title} image'


class Product_details(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=50, blank=True, null=True, default=None)
    # color = models.CharField(max_length=50, blank=True, null=True, default=None)
    video = models.CharField(max_length=200, blank=True, null=True, default=None)
    # internal_storage = models.CharField(max_length=50, blank=True, null=True, default=None)
    external_storage = models.CharField(max_length=50, blank=True, null=True, default=None)
    # ram = models.CharField(max_length=50, blank=True, null=True, default=None)
    production_year = models.CharField(max_length=50, blank=True, null=True, default=None)
    sim_count = models.CharField(max_length=50, blank=True, null=True, default=None)
    sim_type = models.CharField(max_length=50, blank=True, null=True, default=None)
    operation_system = models.CharField(max_length=100, blank=True, null=True, default=None)
    operation_system_version = models.CharField(max_length=100, blank=True, null=True, default=None)
    screen_size = models.CharField(max_length=50, blank=True, null=True, default=None)
    resolution = models.CharField(max_length=50, blank=True, null=True, default=None)
    back_camera = models.CharField(max_length=50, blank=True, null=True, default=None)
    front_camera = models.CharField(max_length=50, blank=True, null=True, default=None)
    battery = models.CharField(max_length=50, blank=True, null=True, default=None)
    weigth = models.CharField(max_length=50, blank=True, null=True, default=None)
    prosessor = models.CharField(max_length=50, blank=True, null=True, default=None)
    security = models.CharField(max_length=50, blank=True, null=True, default=None)
    guarantee = models.CharField(max_length=50, blank=True, null=True, default=None)
    operator_prefix = models.CharField(max_length=50, blank=True, null=True, default=None)
    wifi = models.BooleanField(blank=True, null=True, default=None)
    allow_3G = models.BooleanField(blank=True, null=True, default=None)
    allow_4G = models.BooleanField(blank=True, null=True, default=None)
    nfc = models.BooleanField(blank=True, null=True, default=None)
    gps = models.BooleanField(blank=True, null=True, default=None)
    eye_recognition = models.BooleanField(blank=True, null=True, default=None)
    waterproof = models.BooleanField(blank=True, null=True, default=None)
    faceID = models.BooleanField(blank=True, null=True, default=None)
    shockproof = models.BooleanField(blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.product.title} details'

        
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.id}'

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

