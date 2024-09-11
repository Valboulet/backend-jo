from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["sport_name", "location", "start_date", "end_date", "description", "price"]