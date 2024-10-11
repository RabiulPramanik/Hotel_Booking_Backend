from django.contrib import admin
from . import models

admin.site.register(models.BookingModel)
admin.site.register(models.HotelModel)
admin.site.register(models.LocationModel)
admin.site.register(models.ReviewModel)
admin.site.register(models.RoomModel)
