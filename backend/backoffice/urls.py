from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from rest_framework_simplejwt.views import TokenVerifyView
from .views import CustomRegisterView

from django.urls import path
from . import api

urlpatterns = [
    path('sports/', api.sports_list, name='api_sports_list'),
    path('locations/', api.locations_list, name='api_locations_list'),
    path('events/', api.events_list, name='api_events_list'),
    path('offers/', api.offers_list, name='api_offers_list'),
    path('auth/register/', CustomRegisterView.as_view(), name='rest_register'),
    # path('register/', RegisterView.as_view(), name='rest_register'),
    path('auth/login/', LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
]
