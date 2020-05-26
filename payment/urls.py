from django.urls import path

from .views import *

app_name = 'payment'

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('charge/', charge, name='charge'),
]
