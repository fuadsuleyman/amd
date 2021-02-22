# Generated by Django 3.1.4 on 2021-02-22 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_auto_20210220_1810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_details_property_name',
            options={'verbose_name': 'Property name', 'verbose_name_plural': 'Properties names'},
        ),
        migrations.AlterModelOptions(
            name='product_details_property_value',
            options={'verbose_name': 'Property value', 'verbose_name_plural': 'Properties values'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_published',
        ),
        migrations.AlterField(
            model_name='product',
            name='color_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Color code'),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='Product_details_property_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_details_property_name', to='product.product_details_property_name'),
        ),
        migrations.AlterField(
            model_name='product_details',
            name='product_details_property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_details_properties', to='product.product_details_property_value'),
        ),
        migrations.AlterField(
            model_name='product_details_property_name',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='product_details_property_value',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Title'),
        ),
        migrations.AlterModelTable(
            name='product_details_property_name',
            table='Property name',
        ),
        migrations.AlterModelTable(
            name='product_details_property_value',
            table='Property value ',
        ),
    ]
