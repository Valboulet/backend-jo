from rest_framework import serializers
from .models import Location, Sport, Event, Offer


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = [
            "id_sport",
            "name",
            "pictogram" ,
            "pictogram_url", 
        ]


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = [
            "id_location",
            "name", 
            "image_url", 
        ]


class EventSerializer(serializers.ModelSerializer):
    """Serializer for Event model, transforming event data for API output."""
    
    sport = serializers.CharField(source='sport.name', read_only=True)  # Read-only sport name
    location = serializers.CharField(source='location.name', read_only=True)  # Read-only location name
    event_description = serializers.SerializerMethodField()  # Custom method for event descriptions

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
        """Split the event description string into a list."""
        return [desc.strip() for desc in obj.description.split('|')]  # Split by '|' and trim whitespace


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Offer
        fields = [
            "id_offer",
            "offer_name", 
            "number_of_seats",
            "discount" 
        ]
