from rest_framework import generics
from .models import Car, Booking
from .serializers import CarSerializer, BookingSerializer

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class BookingListCreateView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
