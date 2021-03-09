# Generated by Django 3.1.4 on 2021-03-09 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('order', '0003_auto_20210309_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.customer', verbose_name='')),
            ],
            options={
                'verbose_name': 'checkout',
                'verbose_name_plural': 'checkout',
                'db_table': 'checkout',
            },
        ),
    ]
