from django.db import models

class flight(models.Model):
    flightnumber = models.CharField(max_length=20)
    operatingairline = models.CharField(max_length=22)
    departurecity = models.CharField(max_length=22)
    arrivalcity = models.CharField(max_length=21)
    dateofdeparture = models.DateField()
    estimatedtimeofdeparture = models.TimeField()
    
class passenger(models.Model):
    firstname = models.CharField(max_length=31)
    lastname = models.CharField(max_length=31)
    email = models.EmailField()
    phonenum = models.IntegerField()

class Reservation(models.Model):
    flight = models.OneToOneField(flight,on_delete=models.CASCADE)
    passenger = models.OneToOneField(passenger,on_delete=models.CASCADE)

    

