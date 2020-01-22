from django.db import models

from django.contrib.auth.models import User

class Reservation(models.Model):
  customer_name = models.CharField(max_length=120)
  treatment = models.CharField(max_length=200)
  treatment_description = models.CharField(max_length=480)
  reservation_date = models.DateField()
  reservation_time = models.TimeField()
  reservation_created_date = models.DateTimeField(auto_now_add=True)
  reservation_updated_date = models.DateTimeField(auto_now=True)
  staff_member_name = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Reservation for {self.customer_name} for {self.treatment}"
