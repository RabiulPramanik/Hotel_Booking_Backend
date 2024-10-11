from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, response
from .models import LocationModel, HotelModel, RoomModel, BookingModel, ReviewModel
from .serializers import LocationModelSerializer, HotelModelSerializer, RoomModelSerializer, BookingModelSerializer, BookingCreateSerializer, ReviewCreateSerializer, ReviewListSerializer, ReviewSerializer

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

class BookingListView(generics.ListAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingModelSerializer

class BookingCreateView(generics.CreateAPIView):
    queryset = BookingModel.objects.all()
    serializer_class = BookingCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewCreateView(generics.CreateAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated] 

class ReviewListView(generics.ListAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewListSerializer


# class ReviewUpdateView(generics.UpdateAPIView):
#     queryset = ReviewModel.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [permissions.IsAuthenticated]  # Ensure the user is authenticated to update

#     def perform_update(self, serializer):
#         serializer.save() 

# class ReviewDeleteView(generics.DestroyAPIView):
#     queryset = ReviewModel.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [permissions.IsAuthenticated]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
    
    def perform_update(self, serializer):
        serializer.save()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return response.Response({"detail": "Review deleted successfully"}, status=204)