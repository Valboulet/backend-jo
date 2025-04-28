from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Cart, Location, Sport, Event, Offer, Spectator


class SportSerializer(serializers.ModelSerializer):
    """Serializer for the Sport model."""
    class Meta:
        model = Sport
        fields = [
            "id_sport",
            "name",
            "pictogram",
            "pictogram_url",
        ]


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for the Location model."""
    class Meta:
        model = Location
        fields = [
            "id_location",
            "name",
            "image_url",
        ]


class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model, including related sport and location."""
    sport = serializers.CharField(source='sport.name', read_only=True)
    location = serializers.CharField(source='location.name', read_only=True)
    event_description = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id_event",
            "sport",
            "location",
            "date_start",
            "date_end",
            "event_description",
            "price",
        ]

    def get_event_description(self, obj):
        """Splits the event description into a list of trimmed strings."""
        return [desc.strip() for desc in obj.description.split('|')]


class EventByIdSerializer(serializers.ModelSerializer):
    """Serializer for an unique event, sorted by his id, including related sport and location."""
    sport = serializers.CharField(source='sport.name', read_only=True)
    location = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model =  Event
        fields = [
            "id_event",
            "sport",
            "location",
            "date_start",
        ]


class OfferSerializer(serializers.ModelSerializer):
    """Serializer for the Offer model."""
    class Meta:
        model = Offer
        fields = [
            "id_offer",
            "offer_name",
            "number_of_seats",
            "discount",
        ]


class CartSerializer(serializers.ModelSerializer):
    """Serializer for the Cart model."""
    class Meta:
        model = Cart
        fields = [
            "id_cart",
            "cart_validation_date",
            "user",
        ]



class CustomRegisterSerializer(RegisterSerializer):
    """Custom registration serializer to include additional user fields."""
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)

    def get_cleaned_data(self):
        """Returns the cleaned data with additional fields."""
        data_dict = super().get_cleaned_data()
        data_dict.update({
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        })
        return data_dict
