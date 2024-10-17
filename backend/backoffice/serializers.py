from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Location, Sport, Event, Offer, User, Spectator 

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
    # Déclaration des champs supplémentaires
    date_of_birth = serializers.DateField(required=True)
    firstname = serializers.CharField(max_length=50, required=True)
    lastname = serializers.CharField(max_length=50, required=True)
    country = serializers.CharField(max_length=75, required=True)

    class Meta:
        model = User  # Utilisez le modèle User pour l'enregistrement
        fields = [
            'email',
            'password1',
            'password2',
            'date_of_birth',
            'firstname',
            'lastname',
            'country',
        ]

    def create(self, validated_data):
        # Créez l'utilisateur avec le serializer de base
        user = super().create(validated_data)
        
        # Créez l'objet Spectator en utilisant les données validées
        Spectator.objects.create(
            id_spectator=user.id,
            firstname=validated_data['firstname'],
            lastname=validated_data['lastname'],
            date_of_birth=validated_data['date_of_birth'],
            country=validated_data['country'],
        )
        
        return user
