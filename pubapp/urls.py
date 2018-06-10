from django.urls import path, include
from .views import PubListView, PubDetailView, VenueDetailView, AuthorDetailView, PubRestView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('publication', PubRestView)

urlpatterns = [
    path('', PubListView.as_view(), name='pub_list'),
    path('publication/<int:pk>', PubDetailView.as_view(), name='pub_detail'),
    path('venue/<int:pk>', VenueDetailView.as_view(), name='venue_detail'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author_detail'),
    path('rest/', include(router.urls))
]