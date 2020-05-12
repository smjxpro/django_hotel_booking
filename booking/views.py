from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from booking.forms import BookingForm
from rooms.models import Room


@login_required
def book_room(request, pk):
    if request.method == 'POST':
        booking_form = BookingForm(data=request.POST)

        room = Room.objects.get(pk=pk, available=True)

        print(request.POST.get('check_in_date'))
        # print(booking_form.check_out_date)

        print(booking_form.is_valid())

        if booking_form.is_valid():
            print("valid")

            booking = booking_form.save(commit=False)

            booking.room = room
            booking.customer = request.user.customer

            booking.save()

            room.available = False
            room.save(force_update=True)

            return render(request, 'cart.html', {'booking': booking})
        else:
            print(booking_form.errors)

    else:
        booking_form = BookingForm()

    return render(request, 'book.html', {'booking_form': booking_form, 'pk': pk})


def check_available_rooms_by_number(request):
    if request.method == 'POST':
        adults = request.POST.get('adults')
        children = request.POST.get('children')

        total_persons = int(adults) + int(children)

        print(total_persons)

        available_rooms = Room.objects.filter(available=True, room_type__maximum_capacity__gte=total_persons)

        print(available_rooms)

        return render(request, 'available_rooms.html', {'available_rooms': available_rooms})

    else:
        return HttpResponse(f'Not found!')
