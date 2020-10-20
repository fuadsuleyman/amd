from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    # products = db.relationship('Product', backref='brand', lazy=True)

class Category(models.Model):
    name = models.CharField(max_length=200)
    parent_id = models.IntegerField(default=0)
    description = models.TextField()
    image = models.CharField(max_length=200)
    # products = db.relationship('Product', backref='category', lazy=True)

    # class Category(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    # parent_id = db.Column(db.Integer, nullable=False)
    # name = db.Column(db.String(20), unique=True, nullable=False)
    # description = db.Column(db.Text, nullable=False)
    # image = db.Column(db.String(20), nullable=True)
    # products = db.relationship('Product', backref='category', lazy=True)

class Product(models.Model):
    title = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    price_old = models.IntegerField(default=0)
    description = models.TextField()
    status = models.IntegerField(default=0)
    date_posted = models.DateTimeField('date published')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Product_image(models.Model):
    image = models.CharField(max_length=400)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)