from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationsList(generics.ListCreateAPIView):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer

class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer
