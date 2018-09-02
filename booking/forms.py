from django import forms
from .models import Seat, Booking


class SeatForm(forms.ModelForm):

	class Meta:
		model = Seat
		fields = ('seat_type',)


class BookingForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ('payment_type',)