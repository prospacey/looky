#%%
import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyBGOzhi256VSrfAChm9Kt3BxG8z7aoh0Ds")

# Geocoding an address
geocode_result = gmaps.geocode("3115 Dillon Street, Baltimore, MD")

# Look up an address with reverse geocoding
# reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions(
    "3115 Dillon Street, Baltimore, MD",
    "2007 Portugal Street, Baltimore, MD",
    mode="transit",
    departure_time=now,
)

#%%
print(len(geocode_result))
print(directions_result)
