
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Order, OrderItem
from django.core.mail import send_mail
from account.models import Customer
from django.template.loader import render_to_string




# @receiver(post_save, sender=Order)
def send_form(instance, **kwargs):
    subject= 'Checkout'


    context = {
        'order': instance
    }

    html = render_to_string('checkout-email.html', context)



    send_mail(
        subject=subject,
        message='',
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list=['koki.suleymanov@mail.ru', 'fuadpayme@gmail.com'],
        html_message=html,
        )