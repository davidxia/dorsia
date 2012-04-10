from django.contrib import admin

from dorsianyc.models import Reservation


class ReservationAdmin( admin.ModelAdmin ):
    list_display = ("name", "email", "partySize", "reservationDate", "seatingTime")
    list_filter = ["partySize"]
    search_fields = ["name", "email"]
    date_hierarchy = "reservationDate"

admin.site.register( Reservation, ReservationAdmin )
