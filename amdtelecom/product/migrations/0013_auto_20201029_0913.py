# Generated by Django 3.1.2 on 2020-10-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_details_external_storage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_details',
            name='internal_storage',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='ram',
        ),
        migrations.AddField(
            model_name='product',
            name='internal_storage',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
