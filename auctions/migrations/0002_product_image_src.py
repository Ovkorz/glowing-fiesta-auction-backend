# Generated by Django 4.0.3 on 2022-05-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_src',
            field=models.TextField(blank=True, unique=True),
        ),
    ]
