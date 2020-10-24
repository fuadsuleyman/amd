from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

class Product(models.Model):
    title = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    price_old = models.IntegerField(default=0)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.description}'

class Product_image(models.Model):
    image = models.ImageField(upload_to='uploads/')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.image}'

class Product_details(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size = models.CharField(max_length=50, blank=True, null=True, default=None)
    color = models.CharField(max_length=50, blank=True, null=True, default=None)
    video = models.CharField(max_length=200, blank=True, null=True, default=None)
    internal_storage = models.CharField(max_length=50, blank=True, null=True, default=None)
    ram = models.CharField(max_length=50, blank=True, null=True, default=None)
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
        return f'{self.product_id} details'
