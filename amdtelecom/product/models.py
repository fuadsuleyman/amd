from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.name}, {self.description}'

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.IntegerField(default=0)
    description = models.TextField()
    image = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.name}, {self.description}'

class Product(models.Model):
    title = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    price_old = models.IntegerField(default=0)
    description = models.TextField()
    status = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.description}'

class Product_image(models.Model):
    image = models.FileField(upload_to='uploads/')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)