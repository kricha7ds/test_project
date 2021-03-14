from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework import generics # create a class that inherits from a generic API view
from .models import Room

# API View - view list of all rooms
# Can create a new Room or view all Rooms
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all() # request all Rooms
    serializer_class = RoomSerializer # template to convert data to desired format

