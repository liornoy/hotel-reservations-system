from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Room (models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()
    price_per_night = models.FloatField()
    details = models.TextField()


class Guest (models.Model):
    name = models.CharField(max_length = 120)
    email = models.CharField(max_length = 120)


class Reservation(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    date = models.DateField()


class Review(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                 MaxValueValidator(10)])
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    content = models.TextField
