from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, date
from django.utils import timezone

from product.models import Product


@shared_task
def published_date():
    products = Product.objects.filter(published_expiration__lte=timezone.datetime.today()).update(is_published = False)
