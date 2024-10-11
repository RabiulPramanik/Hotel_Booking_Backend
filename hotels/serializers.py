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

class BookingModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer() 
    room = RoomModelSerializer()

    class Meta:
        model = BookingModel
        fields = [
            'id',
            'user',
            'room',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'NID_number',
            'check_in',
            'check_out',
            'booking_type',
        ]

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingModel
        fields = [
            'room',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'NID_number',
            'check_in',
            'check_out',
        ]
    
    def validate(self, data):
        # Check if check-in date is earlier than check-out date
        if data['check_in'] > data['check_out']:
            raise serializers.ValidationError("Check-in date must be earlier than check-out date.")
        return data
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user.account

        booking = BookingModel.objects.create(user = user, booking_type = 'Upcoming', **validated_data)
        return booking
    

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = [
            'hotel',
            'description',
            'rating',
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user.account

        # Create the review for the specified hotel
        review = ReviewModel.objects.create(user=user, **validated_data)

        hotel = review.hotel
        rating = len(review.rating)
        new_rating = (hotel.rating + rating)/2
        hotel.rating = round(new_rating)
        hotel.save()

        return review

class ReviewListSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    hotel = HotelModelSerializer()

    class Meta:
       model = ReviewModel
       fields = ['id', 'user', 'hotel', 'description', 'rating',] 

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#        model = ReviewModel
#        fields = ['id', 'user', 'hotel', 'description', 'rating',] 



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
        