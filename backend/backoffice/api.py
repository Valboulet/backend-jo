from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Location, Sport, Event, Offer
from .serializers import LocationSerializer, SportSerializer, EventSerializer, OfferSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def sports_list(request):
    """
    Returns the sports list in api
    """
    sports = Sport.objects.all()
    serializer = SportSerializer(sports, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def locations_list(request):
    """
    Returns the locations list in api
    """
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def events_list(request):
    """
    Returns the events list in api
    """
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def offers_list(request):
    """
    Returns the offers list in api
    """
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)

    return JsonResponse({
        'data': serializer.data
    })
