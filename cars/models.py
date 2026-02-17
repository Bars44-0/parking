from django.db import models
from users.models import User

class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    seats = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.model})"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} booked {self.car.name}"

