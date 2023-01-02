import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyBQdAMCKo8vvcmDixiMQXUYVcIrD1y2FXk')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(reverse_geocode_result)