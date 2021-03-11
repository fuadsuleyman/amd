
from django.db.models.signals import post_save, m2m_changed
from django.utils.timezone import now
from django.dispatch import receiver
from .models import Product
from .common import slugify


@receiver(post_save, sender=Product)
def create_product(sender, instance, **kwargs):
    queryset = Category.objects.filter(status=True)
    for category in queryset:  
        print(category, 'sasasaaaaaa')

    instance.slug = f'{slugify(instance.description)}'