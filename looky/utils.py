""" 
Module utils.
Holds utility classes / functions that will be useful for us later.
imported as a name in the global __init__. 
"""


class GeoLo:
    """ Object that holds location information. 
    Address: str
    coords: tuple"""

    # pass in an address, or a longitude/latitude tuple
    # TODO: Maybe -- use `regex` to check if a single input is address or coords, rather than
    # using two arguments to __ini__?
    def __init__(self, address=None, coords=None):
        if address is None and coords is None:
            raise RuntimeError("You must pass an address or longitude/latitude tuple.")
        else:
            self._address = address
            self._coords = coords

    # calling GeoLocation should return the address
    def __repr__(self):
        return self.address

    def address(self, coord):
        """ address closest to the given (lng, lat) coordinates. """
        if self._address:
            return self._address
        else:
            pass  # TODO: use geocode to grab the nearest address to the given coordinates

    def coords(self, address):
        """ (lng, lat) coordinates closest to the given address. """
        if self._coords:
            return self._coords
        else:
            pass  # TODO: use geocode to grab the nearest coordinates to the given address
