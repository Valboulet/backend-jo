from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Cart, Location, Sport, Event, Offer, Ticket, User
from .serializers import CartSerializer, EventByIdSerializer, LocationSerializer, SportSerializer, EventSerializer, OfferSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def sports_list(request):
    """Returns the list of sports in the API."""
    sports = Sport.objects.all()
    serializer = SportSerializer(sports, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def locations_list(request):
    """Returns the list of locations in the API."""
    locations = Location.objects.all()
    serializer = LocationSerializer(locations, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def events_list(request):
    """Returns the list of events in the API."""
    events = Event.objects.all()
    serializer = EventSerializer(events, many=True)

    return JsonResponse({
        'data': serializer.data
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def event_by_id(request, pk):
    """Returns one event by his id."""
    event = Event.objects.get(pk=pk)
    serializer = EventByIdSerializer(event, many=False)

    return JsonResponse(serializer.data)
    


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def offers_list(request):
    """Returns the list of offers in the API."""
    offers = Offer.objects.all()
    serializer = OfferSerializer(offers, many=True)

    return JsonResponse({
        'data': serializer.data
    })



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def offer_by_id(request, pk):
    """Returns one offer by his id."""
    offer = Offer.objects.get(pk=pk)
    serializer = OfferSerializer(offer, many=False)

    return JsonResponse(serializer.data)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_cart(request, pk):
    try:
        user = User.objects.get(pk=pk)

        Cart.objects.create(
            user=user
        )

        return JsonResponse({'Success': True})
    except Exception as e:
        print('Error', e)

        return JsonResponse({'Success': False})
    


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def last_cart_by_id_user(request, user):
    """Returns last cart by id_user."""
    cart = Cart.objects.filter(user=user).order_by("cart_validation_date").last()

    serializer = CartSerializer(cart, many=False)

    return JsonResponse(serializer.data)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_ticket(request, pk, event, offer):
    try:
        event = Event.objects.get(event=event)
        offer = Offer.objects.get(offer=offer)
        cart = Cart.objects.get(pk=pk)

        Ticket.objects.create(
            cart=cart,
            event=event,
            offer=offer
        )

        return JsonResponse({'Success': True})
    except Exception as e:
        print('Error', e)

        return JsonResponse({'Success': False})
    
