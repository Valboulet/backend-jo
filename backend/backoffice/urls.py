from django.urls import path
from . import api

urlpatterns = [
    path('sports/', api.sports_list, name='api_sports_list'),
    path('locations/', api.locations_list, name='api_locations_list'),
]
