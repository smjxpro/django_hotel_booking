from django.shortcuts import render

from booking.models import Booking
from rooms.models import RoomType, Room


def room_type_list(request):
    room_types = RoomType.objects.all()

    return render(request, 'rooms.html', {'room_types': room_types})


def index(request):
    room_types = RoomType.objects.all()

    bookings = Booking.objects.all()

    for booking in bookings:
        booking.days_remaining()

    return render(request, 'index.html', {'room_types': room_types})


def check_available_rooms_by_type(request, pk):
    available_rooms = Room.objects.filter(available=True, room_type_id=pk)

    return render(request, 'available_rooms.html', {'available_rooms': available_rooms})
