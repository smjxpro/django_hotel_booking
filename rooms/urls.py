from django.urls import path

from rooms.views import check_available_rooms_by_type

app_name = 'rooms'

urlpatterns = [
    path('check-available-rooms-by-type/<int:pk>', check_available_rooms_by_type, name='check_available_rooms_by_type')
]
