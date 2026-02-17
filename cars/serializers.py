from rest_framework import serializers
from .models import Car, Booking

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("End date must be after start date")
        return data

