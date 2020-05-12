from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from booking.models import Booking
from customer.forms import UserForm, CustomerForm


def register(request):
    registered = False

    next_page = request.GET.get('next', '/')

    print(next_page)

    if request.user.is_authenticated:
        return HttpResponseRedirect(next_page)
    else:
        if request.method == 'POST':
            user_form = UserForm(data=request.POST)

            customer_form = CustomerForm(data=request.POST)

            if user_form.is_valid() and customer_form.is_valid():
                print("valid")
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                customer = customer_form.save(commit=False)
                customer.user = user

                if 'photo' in request.FILES:
                    print('Photo found!')
                    customer.photo = request.FILES['photo']

                customer.save()

                registered = True

                login(request, user)

                return HttpResponseRedirect(next_page)

            else:
                print(user_form.errors, customer_form.errors)

        else:
            user_form = UserForm()
            customer_form = CustomerForm()

    context = {
        'user_form': user_form,
        'customer_form': customer_form,
        'registered': registered,
    }

    return render(request, 'register.html', context)


def user_login(request):
    next_page = request.GET.get('next', '/')

    print(next_page)

    if request.user.is_authenticated:
        return HttpResponseRedirect(next_page)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user.is_authenticated:
                if user.is_active:
                    login(request, user)

                    return HttpResponseRedirect(next_page)
                else:
                    return HttpResponse('Account inactive!')

            else:
                print('Someone tried to login and failed!')
                print(f'They used username: {username} and password: {password}')

                return HttpResponse('Invalid login details!')

        else:
            return render(request, 'login.html', {'next_page': next_page})


@login_required
def user_logout(request):
    logout(request)
    print(request.path)

    return redirect('customer:login')


@login_required
def customer_dashboard(request):
    bookings = Booking.objects.filter(customer=request.user.customer)
    return render(request, 'dashboard.html', {'bookings': bookings})
