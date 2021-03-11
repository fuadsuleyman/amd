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
    order= Order.objects.get(complete=False)
    items = order.orderitem_set.all()
    print(items, 'items sassasa')

    # total = 0
    imgs = {}

    for item in items:
        imgs.update({item.product.title: item.quantity})
        
    user_form = f'''
        Name: {name}
        Surname: {surname}
        Email: {email}
        Telefon: {num_title}{tel_number}
        Model: {imgs}
    '''
    send_mail(subject, user_form, settings.EMAIL_HOST_USER, ['koki.suleymanov@mail.ru'])