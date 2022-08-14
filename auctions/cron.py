from datetime import datetime
from models import Notification, User, Auction, Product

def add_auction_ended_noti():
    expired_auctions = Auction.objects.filter(status='auction_status_started').filter(end_date__lte=datetime.datetime.now())
    
    for auct in expired_auctions:
        title = "Auction expired!"
        content = f"Your auction - {auct.product.name} - has ended!"
        noti = Notification.objects.create(title=title, content=content, related_to=auct.created_by)
        noti.save()

        auct.update(status='auction_status_expired')
        auct.save()