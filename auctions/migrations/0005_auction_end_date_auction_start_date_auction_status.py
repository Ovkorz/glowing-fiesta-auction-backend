# Generated by Django 4.0.3 on 2022-06-02 23:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction_initial_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auction',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auction',
            name='status',
            field=models.CharField(blank=True, choices=[('auction_status_started', 'Started'), ('auction_status_suspended', 'Suspended'), ('auction_status_awaiting_payment', 'Awaiting Payment'), ('auction_status_finished', 'Finished'), ('auction_status_expired', 'Expired')], max_length=100, null=True),
        ),
    ]