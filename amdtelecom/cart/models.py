from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django import template

from product.models import Product

# Create your models here.

class Cart(models.Model):
    products = models.ManyToManyField(Product, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return f'Cart id: {self.id}'


