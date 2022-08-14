from platform import mac_ver
from pydoc import describe
from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User 

from django.db.models import Max, OuterRef, Subquery, F, Q
import json



# Create your models here.

class Product(models.Model):
    name = models.CharField(blank=False, max_length=50)
    description = models.TextField(blank=True)
    image_src = models.TextField(blank = False)
    

    
    def __str__(self):
        return self.name
    
    def descr (self):
        return self.description


class Auction(models.Model):
    """Model describing a single auction."""

    STATUS_CHOICES = (
        ('auction_status_started','Started'),
        ('auction_status_suspended', 'Suspended'),
        ('auction_status_awaiting_payment', 'Awaiting Payment'),
        ('auction_status_finished', 'Finished'),
        ('auction_status_expired', 'Expired'),
    )
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    initial_price = models.DecimalField(decimal_places=2, max_digits=9, null=False, default=0)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, blank=False, null=False, default='auction_status_started')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=False)
 
    
class Offer(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2,  max_digits=9, null=False, default=0)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)


# class NotificationsManager(models.Manager):
    
#     def notifications_list(self, User):
#         list = Notification.objects.filter(related_to=User)
#         return list


class Notification(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.CharField(max_length=500, blank=False, null=False)
    related_to = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    # objects = NotificationsManager()
