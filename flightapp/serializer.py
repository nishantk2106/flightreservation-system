from rest_framework import serializers
from flightapp.models import flight,passenger,Reservation


class flightserializer(serializers.ModelSerializer):
    class Meta:
        model=flight
        fields= '__all__'
class Passengerserializer(serializers.ModelSerializer):
    class Meta:
        model=passenger
        fields= '__all__'

class Reservationserializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields= '__all__'