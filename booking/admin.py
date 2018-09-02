from django.contrib import admin
from .models import BookedSeat,Booking,Seat
# Register your models here.

admin.site.register(BookedSeat)
admin.site.register(Booking)
admin.site.register(Seat)
