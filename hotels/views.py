from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, response
from .models import LocationModel, HotelModel, RoomModel, BookingModel, ReviewModel
from .serializers import LocationModelSerializer, HotelModelSerializer, RoomModelSerializer, ReviewSerializer, BookingSerializer

class LocationListView(generics.ListAPIView):
    queryset = LocationModel.objects.all()
    serializer_class = LocationModelSerializer

class LocationDetailsView(generics.RetrieveAPIView):
    queryset = LocationModel.objects.all()
    serializer_class = LocationModelSerializer

class HotelListView(generics.ListAPIView):
    queryset = HotelModel.objects.all()
    serializer_class = HotelModelSerializer

class HotelDetailsView(generics.RetrieveAPIView):
    queryset = HotelModel.objects.all()
    serializer_class = HotelModelSerializer
    lookup_field = 'id'

class RoomListVeiw(generics.ListAPIView):
    queryset = RoomModel.objects.all()
    serializer_class = RoomModelSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response({"detail": "Review deleted successfully"}, status=204)
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingModel.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response({"detail": "Booking deleted successfully"}, status=204)