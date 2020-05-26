import stripe
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from booking.models import Booking

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        booking_pk = request.POST['booking-pk']

        context = {'amount': amount,
                   'booking_pk': booking_pk,
                   }
    return render(request, 'payment/checkout.html', context)


def charge(request):
    print('Data:', request.POST)

    booking_pk = request.POST['booking-pk']

    amount = int(float(request.POST['amount']))

    booking = get_object_or_404(Booking, pk=booking_pk)

    if not booking.paid:
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['name'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description=booking,

        )

        booking.paid = True
        booking.booked = True

        booking.room.available = False
        booking.room.save(force_update=True)
        booking.save(force_update=True)

        context = {
            'booking': booking,
            'amount': amount,
        }
        # return render(request, 'payment/charge.html', context)

    else:
        return redirect(
            reverse('customer:dashboard')
        )
