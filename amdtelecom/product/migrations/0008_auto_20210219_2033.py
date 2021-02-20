# Generated by Django 3.1.4 on 2021-02-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210219_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('created_at', 'title'), 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='product_colors',
            name='coler_title',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='product_colors',
            name='color_code',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Title'),
        ),
    ]
