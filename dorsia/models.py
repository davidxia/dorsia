from datetime import datetime

from django.forms import ModelForm
from django.db import models


PARTY_SIZE_CHOICES = zip(range(1, 21), range(1, 21))
SEATING_TIME_CHOICES = ((6, 6), (8, 8))


class Reservation(models.Model):

    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField(blank=False, max_length=254)
    partySize = models.IntegerField(blank=False, choices=PARTY_SIZE_CHOICES)
    reservationDate = models.DateField(blank=False)
    seatingTime = models.PositiveSmallIntegerField(blank=False, choices=SEATING_TIME_CHOICES)
    createdAt = models.DateTimeField(auto_now_add=True, null=True)
    updatedAt = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return "%s, party of %d, %s %d" % (self.name, self.partySize,
                                           datetime.strftime(self.reservationDate, "%Y-%m-%d"),
                                           self.seatingTime)


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
