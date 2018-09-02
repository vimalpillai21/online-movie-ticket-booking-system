from django.conf.urls import url
from .views import payment_gateway, payment_confirmation, reserve_seat,BookingListView,BookingDetailView\
,BookingDeleteView
app_name = 'booking'
urlpatterns = [
    url(r'^seatchoice/(?P<show_id>\d+)/$', reserve_seat, name='reserve_seat'),
    url(r'^payment/$', payment_gateway, name='payment_gateway'),
    url(r'^payment_confirmation/$', payment_confirmation, name='payment_confirmation'),
    url(r'^$', BookingListView.as_view(), name='list'),
    url(r'^(?P<btid>.*)/delete/$', BookingDeleteView.as_view(), name='delete')
 ,   url(r'^(?P<btid>.*)/$', BookingDetailView.as_view(), name='detail'),
#    url(r'^(?P<btid>.*)/delete/$', BookingDeleteView.as_view(), name='delete')
]