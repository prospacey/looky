#%%
import googlemaps
import looky
from datetime import datetime

gmaps = googlemaps.Client(key=looky.API_KEY)

#%%
food_query = gmaps.places(query="food", location=(39.281919, -76.591129), radius=1000)

#%%
type(food_query)
