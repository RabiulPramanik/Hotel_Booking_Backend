from rest_framework import serializers
from .models import LocationModel, HotelModel, RoomModel, BookingModel, ReviewModel
from accounts.serializers import UserModelSerializer

class LocationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationModel
        fields = ['id', 'location', 'descriptions', 'location_image']
    
class HotelModelSerializer(serializers.ModelSerializer):
    main_location = LocationModelSerializer()

    class Meta:
        model = HotelModel
        fields = [
            'id', 
            'name', 
            'descriptions', 
            'out_image', 
            'in_image1', 
            'in_image2', 
            'in_image3', 
            'in_image4', 
            'in_image5', 
            'in_image6', 
            'main_location', 
            'sub_location', 
            'distance', 
            'rating'
        ]

class RoomModelSerializer(serializers.ModelSerializer):
    hotel = HotelModelSerializer()
    
    class Meta:
        model = RoomModel
        fields = [
            'id', 
            'hotel', 
            'room_no', 
            'room_type', 
            'room_image', 
            'price'
        ]

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = ['id', 'user', 'room', 'first_name', 'last_name', 'email', 'phone_number', 'NID_number', 'check_in', 'check_out', 'booking_type']

    def create(self, validated_data):
        booking = BookingModel.objects.create(**validated_data)
        booking.save()
        return booking
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.NID_number = validated_data.get('NID_number', instance.NID_number)
        instance.check_in = validated_data.get('check_in', instance.check_in)
        instance.check_out = validated_data.get('check_out', instance.check_out)
        instance.booking_type = validated_data.get('booking_type', instance.booking_type)
        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['id', 'user', 'hotel', 'description', 'rating']

    def create(self, validated_data):
        review = ReviewModel.objects.create(**validated_data)
        review.save()
        hotel = review.hotel
        rating = len(review.rating)
        new_rating = (hotel.rating + rating)/2
        hotel.rating = round(new_rating)
        hotel.save()
        return review
    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        hotel = instance.hotel
        rating = len(instance.rating)
        new_rating = (hotel.rating + rating)/2
        hotel.rating = round(new_rating)
        hotel.save()
        return instance
        