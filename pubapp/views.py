from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models

# Create your views here.

class PubListView(ListView):
    model = models.Publication
    

class PubDetailView(DetailView):
    model = models.Publication

    
class VenueDetailView(DetailView):
    model = models.Venue

class AuthorDetailView(DetailView):
    model = models.Author