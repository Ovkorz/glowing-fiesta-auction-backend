from fileinput import FileInput
from auctions.views import OfferViewSet, auctionDetail, auctionList, auctionNew, notificationDetail, notificationList, userViewSet
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns


# router.register(r'new', )

urlpatterns = [
    path('', auctionList.as_view()),
    path('new', auctionNew.as_view()),
    path('<int:pk>', auctionDetail.as_view()),
    path('users/', userViewSet.as_view({'get': 'list'})),
    path('users/<int:pk>/', userViewSet.as_view({'get': 'retrieve'}),),
    path('offers', OfferViewSet.as_view({'post': 'create'})),
    path('notifications', notificationList.as_view()),
    path('notifications/<int:pk>', notificationDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)