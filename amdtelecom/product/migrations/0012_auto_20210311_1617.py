# Generated by Django 3.1.4 on 2021-03-11 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_product_published_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='internal_storage',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Daxili yaddaş'),
        ),
    ]
