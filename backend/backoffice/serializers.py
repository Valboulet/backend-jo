from rest_framework import serializers
from .models import Location, Sport


class SportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sport
        fields = [
            "id_sport",
            "name", 
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