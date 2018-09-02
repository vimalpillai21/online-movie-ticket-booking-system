from django.conf.urls import url
from .views import TheatreListView, theatre_details
app_name = 'theatre'
urlpatterns = [
    url(r'^$', TheatreListView.as_view(), name='list'),
    url(r'^(?P<theatre_id>\d+)/$', theatre_details, name='detail')   
]