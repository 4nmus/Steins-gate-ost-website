from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render
from .models import Songs
# Create your views here.


class HomeView(ListView):
    model = Songs
    template_name = 'front/base.html'
    context_object_name = 'threads'
    paginate_by = 4
    ordering = ['date']
    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['songs'] = Songs.objects.all()

        return ctx
class SongView(ListView):
    model = Songs
    template_name = "front/base.html"
    context_object_name = 'songs'

    def get_context_data(self, **kwargs):
        ctx = super(SongView, self).get_context_data(**kwargs)
        ctx['song'] = Songs.objects.get(pk=self.kwargs['pk'])
        return ctx