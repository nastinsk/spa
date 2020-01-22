from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer
from .permissions import IsAuthorOrReadOnly

class ReservationsList(generics.ListCreateAPIView):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer
  
class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer
  permission_classes = (IsAuthorOrReadOnly, )

