from rest_framework import serializers

from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reservation
    fields = [
      'id', 'customer_name', 'treatment','treatment_description','reservation_date','reservation_time','reservation_created_date', 'reservation_updated_date', 'staff_member_name'
      ]