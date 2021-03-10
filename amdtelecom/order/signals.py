
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail




@receiver(post_save, sender=Order)
def send_form(sender, instance, **kwargs):
    subject= 'Checkout'
    name = instance.name
    surname = instance.surname
    email = instance.email
    num_title = instance.num_title
    tel_number = instance.tel_number
    instance.complete = True
    # print(instance.order_items.all(), 'orderitems')

    user_form = f'''
        Name: {name}
        Surname: {surname}
        Email: {email}
        Telefon: {num_title}{tel_number}
    '''

    send_mail(subject, user_form, settings.EMAIL_HOST_USER, ['koki.suleymanov@mail.ru'])