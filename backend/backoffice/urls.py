from django.urls import path
from . import api

urlpatterns = [
    path('sports/', api.sports_list, name='api_sports_list'),
    path('locations/', api.locations_list, name='api_locations_list'),
    path('events/', api.events_list, name='api_events_list'),
    path('offers/', api.offers_list, name='api_offers_list'),
]
