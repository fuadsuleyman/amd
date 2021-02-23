
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Checkout
from django.core.mail import send_mail



@receiver(post_save, sender=Checkout)
def send_form(sender, instance, **kwargs):
    name = instance.name
    surname = instance.surname
    email = instance.email
    num_title = instance.num_title
    tel_number = instance.tel_number

    user_form = f'''
        Name: {name}
        Surname: {Surname}
        Email: {email}
        Telefon: {num_title} {tel_number}
    '''

    send_mail(subject, user_form, 'husubayli@gmail.com', ['koki.suleymanov@mail.ru'])