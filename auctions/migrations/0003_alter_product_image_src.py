# Generated by Django 4.0.3 on 2022-05-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_product_image_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_src',
            field=models.TextField(blank=True),
        ),
    ]
