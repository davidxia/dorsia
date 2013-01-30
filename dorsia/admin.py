from django.contrib import admin

from dorsia.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "partySize", "reservationDate", "seatingTime", "createdAt", "updatedAt")
    list_filter = ["partySize"]
    search_fields = ["name", "email"]
    date_hierarchy = "reservationDate"

admin.site.register(Reservation, ReservationAdmin)
