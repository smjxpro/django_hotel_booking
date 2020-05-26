from django.contrib import admin
from django.contrib.admin import ModelAdmin

from rooms.models import RoomType, Room


class RoomTypeAdmin(ModelAdmin):
    list_display = (
        '__str__', 'maximum_capacity', 'price',)


class RoomAdmin(ModelAdmin):
    list_display = (
        '__str__', 'room_no', 'room_type', 'available',)

    list_filter = ('available',)


admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
