from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render
from .models import Song
# Create your views here.


def HomeView(request):
    songs = Song.objects.all()
    num = songs.count()
    context = {'forums': songs, 'count': num,}
    return render(request, 'front/home.html', context)