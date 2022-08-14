from rest_framework import mixins, permissions, generics, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


from django.contrib.auth.models import User
from django import middleware
from django.db.models import Count, Max, F
from django.db.models.functions import Greatest

from auctions.permissions import IsOwnerOrReadOnly
from auctions.serializers import AuctionSerializerNew, NotificationSerializer, TokenSerializer, AuctionListSerializer, AuctionSerializerDetail, UserSerializer, OfferSerializer
from auctions.models import Auction, Notification, Offer

# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token

# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


class auctionList(  mixins.ListModelMixin,
                    generics.GenericAPIView):
    
    queryset = Auction.objects.all().annotate(number_of_offers=Count('offer__auction'), 
                                              current_price = Max('offer__price'),  
                                              created_by_username = F('created_by__username'))
    serializer_class = AuctionListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
class auctionDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    
    queryset = Auction.objects.all().annotate(number_of_offers=Count('offer__auction'), 
                                              current_price = Max('offer__price'),  
                                              created_by_username = F('created_by__username'))

    serializer_class = AuctionSerializerDetail
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class auctionNew(APIView):
    queryset = Auction.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = AuctionSerializerNew(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by = self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class userViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class notificationList( generics.GenericAPIView ):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Notification.objects.all()


    def get(self, request):
        notifications = self.get_queryset().filter(related_to=self.request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)

class notificationDetail( generics.GenericAPIView, mixins.DestroyModelMixin):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
  
# class CustomAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
        # serializer = self.serializer_class(data=request.data,
        #                                    context={'request': request})
        # serializer.is_valid(raise_exception=True)
        # user = serializer.validated_data['user']
        # token, created = Token.objects.get_or_create(user=user)
        # # return Response({
        #     'token': token.key,
        #     'user_id': user.pk,
        #     'email': user.email
        # })
  
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(bidder=self.request.user)



