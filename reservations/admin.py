from django.contrib import admin
from .models import Guest, Reservation, Room, Review


admin.site.register(Guest)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Review)
