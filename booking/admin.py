from django.contrib import admin
from django.contrib.admin import ModelAdmin

from booking.models import Booking


class BookingAdmin(ModelAdmin):
    list_display = (
        '__str__', 'customer', 'room', 'booking_date', 'booking_price', 'paid', 'total_days', 'days_remaining')


admin.site.register(Booking, BookingAdmin)
