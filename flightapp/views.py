from django.shortcuts import render
from flightapp.models import passenger,flight,Reservation
from flightapp.serializer import Passengerserializer,flightserializer,Reservationserializer
from rest_framework import viewsets

class flightviewsets(viewsets.ModelViewSet):
    queryset= flight.objects.all()
    serializer_class = flightserializer

class passengerviewsets(viewsets.ModelViewSet):
    queryset = passenger.objects.all()
    serializer_class = Passengerserializer

class reservationviewsets(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = Reservationserializer