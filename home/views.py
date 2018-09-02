from django.shortcuts import render
from django.views.generic import View, CreateView
from movie.models import Movie
from .forms import RegisterForm
# Create your views here.
class ShowIndex(View):
    def get(self,request,*args,**kwargs):
        movie_list = Movie.objects.all().order_by('popularity_index')
        top_movie  = Movie.objects.all().order_by('popularity_index')[:3]
        context = {'movie_list':movie_list,'top_movie':top_movie}
        return render(request,'home.html',context)

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'
