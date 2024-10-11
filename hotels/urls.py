from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, basename='review')


urlpatterns = [
    path('locations/list/', views.LocationListView.as_view(), name="location-list"),
    path('locations/<int:pk>/', views.LocationDetailsView.as_view(), name="location-details"),
    path('hotels/list/', views.HotelListView.as_view(), name="hotel-list"),
    path('hotels/<int:id>/', views.HotelDetailsView.as_view(), name="hotel-details"),
    path('rooms/list/', views.RoomListVeiw.as_view(), name="room-list"),
    path('booking/list/', views.BookingListView.as_view(), name="booking-list"),
    path('booking/create/', views.BookingCreateView.as_view(), name="booking-create"),
    path('review/create/', views.ReviewCreateView.as_view(), name="review-create"),
    path('review/list/', views.ReviewListView.as_view(), name="review-list"),
    # path('review/list/<int:pk>/', views.ReviewUpdateView.as_view(), name="review-update"),
    # path('review/list/<int:pk>/delete', views.ReviewDeleteView.as_view(), name="review-delete"),
    path('', include(router.urls)),

]
