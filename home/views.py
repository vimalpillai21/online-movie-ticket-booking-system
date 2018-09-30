from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.generic import View, CreateView, FormView, ListView
from movie.models import Movie
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .forms import RegisterForm, LoginForm
# Create your views here.
class ShowIndex(View):
    def get(self,request,*args,**kwargs):
        movie_list = Movie.objects.all().order_by('popularity_index')
        top_movie  = Movie.objects.all().order_by('popularity_index')[:3]
        context = {'movie_list':movie_list,'top_movie':top_movie}
        return render(request,'home.html',context)

class SearchView(ListView):
    template_name = 'search.html'
    
    def get_context_data(self,*args, **kwargs):
        context = super(SearchView,self).get_context_data(*args,**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
    
    def get_queryset(self,*args,**kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            query = query.strip()
            return Movie.objects.search(query)
        else:
            return Movie.objects.all()

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/'

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'registration/login.html'
    success_url = '/'
    
    def form_valid(self,form):
        request = self.request
        next_ = request.GET.get("next")
        next_post = request.POST.get("next")
        redirect_path   =   next_ or next_post or None
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request,username=email,password=password)
        if user is not None:
            print(user)
            login(request,user)
            if is_safe_url(redirect_path,request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")
        #print(form.non_field_errors)
        # s = super(FormView,self).form_invalid(form)
        # s.add 
        return self.form_invalid(form) 
    def form_invalid(self,form):
        form.add_error(None,"Username and password dont match")
        return super(FormView,self).form_invalid(form)
    
        
