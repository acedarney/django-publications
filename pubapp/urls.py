from django.urls import path
from .views import PubListView

urlpatterns = [
    path('', PubListView.as_view(), name='pub_list'),
]