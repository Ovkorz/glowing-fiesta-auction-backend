from dataclasses import field
from locale import currency
from math import prod
from pickletools import read_long1
from pyexpat import model
from unicodedata import decimal
from venv import create
from rest_framework import serializers, fields
from auctions.models import Auction, Notification, Product, Offer
from django.contrib.auth.models import User
from datetime import date, datetime



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image_src']


class ProductSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image_src']


class AuctionSerializerDetail(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    created_by= serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    number_of_offers = serializers.IntegerField()
    current_price = serializers.DecimalField(max_digits=7, decimal_places=2)


    class Meta:
        model = Auction
        fields = ['id', 'product', 'created_by', 'current_price','initial_price', 'number_of_offers','end_date']
        
        
class AuctionSerializerNew(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    end_date = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    
    def create(self, validated_data):
        product_data = validated_data['product']
        product_serializer = ProductSerializer(data=product_data)
        product_serializer.is_valid(raise_exception=True)
        # product_serializer.validate_unique()
        product = product_serializer.save()
        validated_data['product'] = product
        
        # validated_data['end_date'] = datetime.strptime(validated_data['end_date'], "%d/%m/%Y %H:%M:%S")
        
        return Auction.objects.create(**validated_data)
    
    class Meta:
        model = Auction
        fields = ['product', 'initial_price', 'end_date']


class AuctionListSerializer(serializers.ModelSerializer):
    
    number_of_offers = serializers.IntegerField()
    current_price = serializers.IntegerField()
    created_by_username = serializers.CharField()
    
    product = ProductSerializerList()
    
    
    def create(self, validated_data):
        return Auction.objects.create(**validated_data)
    
    class Meta:
        model = Auction
        fields = ['id', 'product', 'created_by_username', 'initial_price','current_price', 'number_of_offers', 'end_date']
        

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)


class OfferSerializer(serializers.ModelSerializer):
    bidder = serializers.PrimaryKeyRelatedField(required=False, read_only=True)

    def create(self, validated_data):
        return Offer.objects.create(**validated_data)

    class Meta:
        model = Offer
        fields = ['id','bidder', 'price', 'auction']


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['id', 'title', 'content', 'related_to']