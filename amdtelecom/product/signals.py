
from django.db.models.signals import pre_save
from django.utils.timezone import now
from django.dispatch import receiver
from .models import Category
from .common import slugify


@receiver(pre_save, sender=Category)
def create_product(sender, instance, **kwargs):
    
    instance.slug = f'{slugify(instance.title)}'