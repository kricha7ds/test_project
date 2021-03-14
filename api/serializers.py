# Take our model (Room) and translate it into a JSON response
from rest_framework import serializers
from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:

        model = Room # define model to serialize
        fields = ('id', 'code', 'host', 'guest_can_pause', # define all fields we'd like to see in the serialization
                    'votes_to_skip', 'created_at') 