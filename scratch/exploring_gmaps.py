#%%
import googlemaps
from pathlib import Path

# Create googlemaps.Client object gmaps.
API_key_filePath = Path('/mnt/c/Users/devin/Documents/GitHub/prospacey/looky/API_key.txt')
with open(API_key_filePath, 'r') as API_key_file:
    gmaps = googlemaps.Client(key=API_key_file.readline())


def places():
    # query = gmaps.find_place(input='food', input_type='textquery', fields=name)
    query = gmaps.places(query='food', location=(39.281919, -76.591129), radius=50)

    return query

#%%

q = places()
res = q['results']
print(*res[0].keys(), sep='\n')