from django.db import models
import string
import random


# TODO: modify random code generator to generate code with alternating pattern of letters and numbers

# function to generate key for Room entry
def generate_unique_code():
    length = 6
    # generate random code
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        # ensure that all keys are unique by verifying against database
        if Room.objects.filter(code = code).count() == 0:
            break

    return code

# ROOM model that will host participating users
class Room(models.Model):
    code = models.CharField(max_length = 8, default = generate_unique_code, unique = True) # unique key to join a Room
    host = models.CharField(max_length = 50, unique = True) # to track session key
    guest_can_pause = models.BooleanField(null = False, default = False) # permission to enable/disable pausing functionality by guests
    votes_to_skip = models.IntegerField(null = False, default = 1)
    created_at = models.DateTimeField(auto_now_add = True) 
