from django.shortcuts import render,redirect
from .models import Movie
from .forms import MovieForm
# Create your views here.

def index_view(request):
    return render(request,'testapp/index.html')


def movie_view(request):
    movies_list=Movie.objects.all()
    return render(request,'testapp/movie.html',{'movies_list':movies_list})


def add_movie(request):
     form=MovieForm()
     submitted=False
     if request.method=='POST':
         form=MovieForm(request.POST)
         if form.is_valid():
             form.save()
             submitted=True
     return render(request,'testapp/movie_form.html',{'form':form,'submitted':submitted})