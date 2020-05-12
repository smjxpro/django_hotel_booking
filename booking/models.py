from datetime import datetime

from django.db import models

from customer.models import Customer
from rooms.models import Room


class Booking(models.Model):
    customer = models.ForeignKey(Customer, related_name='booking', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='booking', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    paid = models.BooleanField(default=False)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.customer.user.username}_{self.pk}'

    def booking_price(self):
        return self.room.room_type.price * (self.check_out_date.day - self.check_in_date.day)

    def total_days(self):
        return self.check_out_date.day - self.check_in_date.day

    def days_remaining(self):
        if self.check_out_date.day >= datetime.now().day:
            return self.check_out_date.day - datetime.now().day
        else:
            self.room.available = True

            self.room.save()

            return 0
