# Generated by Django 3.1.4 on 2021-03-09 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210309_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_details',
            name='product_details_propert_value',
        ),
    ]
