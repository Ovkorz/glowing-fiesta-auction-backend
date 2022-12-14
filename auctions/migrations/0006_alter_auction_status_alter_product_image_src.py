# Generated by Django 4.0.3 on 2022-06-03 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auction_end_date_auction_start_date_auction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='status',
            field=models.CharField(choices=[('auction_status_started', 'Started'), ('auction_status_suspended', 'Suspended'), ('auction_status_awaiting_payment', 'Awaiting Payment'), ('auction_status_finished', 'Finished'), ('auction_status_expired', 'Expired')], default='auction_status_started', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_src',
            field=models.TextField(),
        ),
    ]
