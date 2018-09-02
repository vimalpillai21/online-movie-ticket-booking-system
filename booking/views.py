from django.shortcuts import render, get_object_or_404
from .models import Booking, BookedSeat, Seat
from theatre.models import Show
from .forms import SeatForm, BookingForm
from django.urls import reverse_lazy
#from django.views.generic import CreateView
import datetime
from django.views.generic import ListView,DetailView,DeleteView
from theatre.models import Theatre
from django.shortcuts import redirect
from django.http.response import Http404

# Create your views here.

def reserve_seat(request, show_id):
    try:
        show_info = Show.objects.get(pk=show_id)
    except Theatre.DoesNotExist:
        raise Http404("Page does not exist")
    form = SeatForm()
    return render(request, 'reserve_seat.html', 
        {'show_info': show_info, 'form': form})


def payment_gateway(request):
    if request.POST:
        seats = request.POST.get('selected_seat')
        seat_type = request.POST.get('seat_type')
        show_id = request.POST.get('show_id')

        show = Show.objects.get(pk=show_id)
        seats = seats.split(',')
        book_seat = []
        for each in seats:
            if Seat.objects.filter(no=each, show=show).exists():
                return render(request, 'reserve_seat.html', 
                    {'show_info': show, 'form': SeatForm()})
            s = Seat(no=each, seat_type=seat_type, show=show)
            book_seat.append(s)
        Seat.objects.bulk_create(book_seat)

        form = BookingForm()

        price_dict = {'Platinum': 300, 'Gold': 200, 'Silver': 100}
        ticket_price = price_dict[seat_type]*len(book_seat)

        seat_str = ""
        for i in range(0, len(seats)):
            if i == len(seats)-1:
                seat_str += seats[i]
            else:
                seat_str += seats[i] + ','

        return render(request, 'payment_gateway.html', 
            {'seats': seat_str, 'seat_type': seat_type, 
            'show': show, 'form': form, 'ticket_price': ticket_price})
    else:
        return redirect('theatre.views.theatre_list')


def payment_confirmation(request):
    if request.POST:
        show_id = request.POST.get('show_id')
        show = Show.objects.get(pk=show_id)
        seats = request.POST.get('selected_seat')
        seats = seats.split(',')
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payment_type = request.POST.get('payment_type')
        paid_amount = request.POST.get('amount')
        paid_by = request.user
        id = str(show) + str(seats) + timestamp
        book = Booking(id=id, timestamp=timestamp, payment_type=payment_type, 
            paid_amount=paid_amount, paid_by=paid_by)
        book.save()

        booked_seat = []

        for seat in seats:
            print(seat)
            s = Seat.objects.get(no=seat, show=show)
            b = Booking.objects.get(pk=id)
            booked = BookedSeat(seat=s, booking=b)
            booked_seat.append(booked)

        BookedSeat.objects.bulk_create(booked_seat)

        return render(request, 'payment_confirmation.html')
    else:
        return redirect('theatre.views.theatre_list')


class BookingListView(ListView):
    def get_queryset(self):
        return Booking.objects.filter(paid_by=self.request.user)
    
class BookingDetailView(DetailView):
    def get_queryset(self):
        return Booking.objects.filter(paid_by=self.request.user)
    
    def get_object(self,*args,**kwargs):
        btid = self.kwargs.get('btid')
        obj = get_object_or_404(Booking,id=btid)
        return obj

class BookingDeleteView(DeleteView):
    model = Booking
    success_url = reverse_lazy('booking:list')    
    def get_object(self,*args,**kwargs):
        btid = self.kwargs.get('btid')
        obj = get_object_or_404(Booking,id=btid)
        return obj
