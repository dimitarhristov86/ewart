# Generated by Django 4.0.4 on 2022-05-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_available_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default='On stock'),
        ),
    ]
