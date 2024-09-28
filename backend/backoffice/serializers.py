from rest_framework import serializers
from .models import Location, Sport, Event


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

    class Meta:
        model = Event
        fields = [
            "id_event",
            "sport", 
            "location",
            "date_start",
            "date_end",
            "description",
            "price", 
        ]