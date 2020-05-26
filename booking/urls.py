from django.urls import path

from booking.views import *

app_name = 'booking'

urlpatterns = [
    path('book/<int:pk>', book_room, name='book'),
    path('delete-booking/', delete_booking, name='delete_booking'),
    path('check-available-rooms/', check_available_rooms_by_number, name='check_available_rooms_by_number'),
]
