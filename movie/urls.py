from django.conf.urls import url
from .views import MovieListView, movie_details

app_name = 'movie'

urlpatterns = [
    
    url(r'^$', MovieListView.as_view(), name='list'),
    url(r'^(?P<movie_id>\d+)/$', movie_details, name='detail'),
        
]