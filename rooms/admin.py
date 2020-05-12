from django.contrib import admin

from rooms.models import RoomType, Room

admin.site.register(RoomType)
admin.site.register(Room)
