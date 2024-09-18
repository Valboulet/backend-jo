from django.urls import path
from . import api

urlpatterns = [
    path('', api.sports_list, name='api_sports_list'),
]
