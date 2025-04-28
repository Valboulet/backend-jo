from django.urls import path
from . import api

from dj_rest_auth.jwt_auth import get_refresh_view
# from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView
from .views import CustomRegisterView
from rest_framework_simplejwt.views import TokenVerifyView

# from .views import StripeCheckoutView


urlpatterns = [
    path('sports/', api.sports_list, name='api_sports_list'),
    path('locations/', api.locations_list, name='api_locations_list'),

    path('events/', api.events_list, name='api_events_list'),
    path('event/<int:pk>', api.event_by_id, name='api_event_by_id'),

    path('offers/', api.offers_list, name='api_offers_list'),
    path('offer/<int:pk>', api.offer_by_id, name='api_offer_by_id'),


    path('auth/register/', CustomRegisterView.as_view(), name='custom_register'),
    path('auth/login/', LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    # path('create-checkout-session/', StripeCheckoutView.as_view(), name='create_checkout_session'),

    path('create_cart/<uuid:pk>/', api.create_cart, name='api_create_cart'),

    path('cart/<str:user>', api.last_cart_by_id_user, name='api_last_cart_by_id_user'),

    path('create_ticket/<uuid:pk>/<str:event>/<str:offer>/', api.create_ticket, name='api_create_ticket'),

]
