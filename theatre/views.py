from django.shortcuts import render
from .models import Theatre, Show
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404,Http404
import datetime
# Create your views here.
class TheatreListView(ListView):
    def get_queryset(self):
        return Theatre.objects.all()
    
    
    def get_context_data(self, *args, **kwargs):
        context = super(TheatreListView,self).get_context_data(*args,**kwargs)
        theatres = Theatre.objects.all().order_by('city')
        theatre_list = []
        theatre_by_city = []
        city = theatres[0].city
        for i in range(0,len(theatres)):
            if city != theatres[i].city:
                city = theatres[i].city
                theatre_list.append(theatre_by_city)
                theatre_by_city =[]
            theatre_by_city.append(theatres[i])
        theatre_list.append(theatre_by_city)
        print(theatre_list)
        
        context['theatres'] = theatre_list
        return context
        
#class TheatreDetailView(DetailView):
#    def get_queryset(self):
#        return Theatre.objects.all()
#    
#    show_list=[]
#    show_by_movie = []
#    
#        
#    def get_context_data(self,*args, **kwargs):
#        context = super(TheatreDetailView,self).get_context_data(*args,**kwargs)
#        rest_id = self.kwargs.get("pk")
#        obj = get_object_or_404(Theatre,id=rest_id)
#        
#         
#        shows = Show.objects.filter(theatre=obj,date=datetime.date.today()).order_by('movie')
#        movie = shows[0].movie
#        for i in range(0,len(shows)):
#            if movie != shows[i].movie:
#                movie = shows[i].movie
#                self.show_list.append(self.show_by_movie)
#                self.show_by_movie = []
#            self.show_by_movie.append(shows[i])
#        self.show_list.append(self.show_by_movie)
        
        
    
#        context['show_list'] = self.show_list
        #print(context)
#        return context
def theatre_details(request, theatre_id):
    try:
        theatre_info = Theatre.objects.get(pk=theatre_id)
        shows = Show.objects.filter(theatre=theatre_id, 
            date=datetime.date.today()).order_by('movie')

        show_list = []
        if shows:
            show_by_movie = []
            movie = shows[0].movie
            for i in range(0, len(shows)):
                if movie != shows[i].movie:
                    movie = shows[i].movie
                    show_list.append(show_by_movie)
                    show_by_movie = []
                show_by_movie.append(shows[i])
    
            show_list.append(show_by_movie)
    
        print(show_list)

    except Theatre.DoesNotExist:
        raise Http404("Page does not exist")
    return render(request, 'theatre/theatre_detail.html', 
        {'theatre_info': theatre_info, 'show_list': show_list})
        