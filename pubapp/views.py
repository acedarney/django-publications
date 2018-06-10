from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from .serializers import PublicationSerializer
from . import models

class PubListView(ListView):
    model = models.Publication
    

class PubDetailView(DetailView):
    model = models.Publication

    
class VenueDetailView(DetailView):
    model = models.Venue


class AuthorDetailView(DetailView):
    model = models.Author


class PubRestView(viewsets.ModelViewSet):
    queryset = models.Publication.objects.all()
    serializer_class = PublicationSerializer
