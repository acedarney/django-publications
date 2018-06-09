from django.views.generic.list import ListView
from . import models

# Create your views here.

class PubListView(ListView):
    model = models.Publication