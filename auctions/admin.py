from django import views
from django.contrib import admin

from auctions.models import Auction, Notification, Product, Offer


# Register your models here.
class AuctionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'created_by')
    pass


class OfferAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    pass

class NotificationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Auction, AuctionAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Notification, NotificationAdmin)