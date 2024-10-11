from django.db import models
from accounts.models import UserModel

class LocationModel(models.Model):
    location = models.CharField(max_length=100)
    descriptions = models.TextField()
    location_image = models.ImageField(upload_to="hotels/location_images/")

    def __str__(self):
        return self.location

class HotelModel(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()

    out_image = models.ImageField(upload_to="hotels/out_images/")
    in_image1 = models.ImageField(upload_to="hotels/in_images/", null=True, blank=True)
    in_image2 = models.ImageField(upload_to="hotels/in_images/", null=True, blank=True)
    in_image3 = models.ImageField(upload_to="hotels/in_images/", null=True, blank=True)
    in_image4 = models.ImageField(upload_to="hotels/in_images/", null=True, blank=True)
    in_image5 = models.ImageField(upload_to="hotels/in_images/", null=True, blank=True)
    in_image6 = models.ImageField(upload_to="hotels/in_images/", null=True, blank=True)

    main_location = models.ForeignKey(LocationModel, related_name="hotel", on_delete=models.CASCADE)
    sub_location = models.CharField(max_length=100)
    distance = models.IntegerField(default=0)

    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name

Room_CHOICES = [
    ('Single', 'Single'),
    ('Double', 'Double'),
]
class RoomModel(models.Model):
    hotel = models.ForeignKey(HotelModel, related_name="room", on_delete=models.CASCADE)
    room_image = models.ImageField(upload_to="hotels/room_images/")
    room_no = models.IntegerField(default=0)
    room_type= models.CharField(choices = Room_CHOICES, max_length = 10)
    price = models.IntegerField(default=5)

    def __str__(self):
        return f"{str(self.room_no)} {self.room_type} for {self.hotel.name}"

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class ReviewModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='review', on_delete=models.CASCADE)
    hotel = models.ForeignKey(HotelModel, related_name='review', on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)

    def __str__(self):
        return self.user.user.username

BOOKING_TYPE = [
    ('Completed', 'Completed'),
    ('Upcoming', 'Upcoming'),
    ('Runing', 'Runing'),
]
class BookingModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='booking', on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel, related_name='booking', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=12)
    NID_number = models.CharField(max_length=20)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    booking_type = models.CharField(choices = BOOKING_TYPE, max_length = 10, null=True, blank=True)

    def __str__(self):
        return str(self.NID_number)





