
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf.urls import url,include
from home.views import ShowIndex, RegisterView
from home.forms import LoginForm
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$',LoginView.as_view(authentication_form=LoginForm),name = 'login'),
    url(r'^logout/$',LogoutView.as_view(),name = 'logout'),
    url(r'^$', ShowIndex.as_view()),
    url(r'^movies/', include('movie.urls',namespace='movie')),
    url(r'^booking/', include('booking.urls',namespace='booking')),
    url(r'^theatres/', include('theatre.urls',namespace='theatre')),
    url(r'^register/$',RegisterView.as_view(),name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)