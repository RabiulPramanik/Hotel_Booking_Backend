from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, basename='review')
router.register(r'bookings', views.BookingViewSet, basename='booking')


urlpatterns = [
    path('locations/list/', views.LocationListView.as_view(), name="location-list"),
    path('locations/<int:pk>/', views.LocationDetailsView.as_view(), name="location-details"),
    path('hotels/list/', views.HotelListView.as_view(), name="hotel-list"),
    path('hotels/<int:id>/', views.HotelDetailsView.as_view(), name="hotel-details"),
    path('rooms/list/', views.RoomListVeiw.as_view(), name="room-list"),
    path('', include(router.urls)),

]
