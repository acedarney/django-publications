from django.urls import path
from .views import PubListView, PubDetailView, VenueDetailView, AuthorDetailView

urlpatterns = [
    path('', PubListView.as_view(), name='pub_list'),
    path('publication/<int:pk>', PubDetailView.as_view(), name='pub_detail'),
    path('venue/<int:pk>', VenueDetailView.as_view(), name='venue_detail'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
]