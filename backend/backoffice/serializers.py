from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Location, Sport, Event, Offer, Spectator

class SportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sport
        fields = [
            "id_sport",
            "name",
            "pictogram",
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
        return [desc.strip() for desc in obj.description.split('|')]



class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = [
            "id_offer",
            "offer_name", 
            "number_of_seats",
            "discount" 
        ]


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict.update({
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        })
        return data_dict