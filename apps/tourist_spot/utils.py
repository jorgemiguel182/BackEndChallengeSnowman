import geocoder
from decouple import config
from django.db.models import Q
from geopy.distance import great_circle

from apps.core.models import TbTouristSpot


def calculate_distance_great_circle_in_km(lat1, long1, lat2, long2):
    """
    Calculate the distance of the parameters lat1/long1 over lat2/long2 using The great-circle distance,
    is the shortest distance between two points on the surface of a sphere

    :param lat1: String > Latitude of location
    :param long1:String > Longitude of location
    :param lat2: String > Latitude of location
    :param long2:String > Longitude of location
    :return: Distance in KM of two spots
    """
    if not lat1 or not long1 or not lat2 or not long2:
        raise Exception('Mandatory parameters not informed')

    return great_circle((lat1, long1), (lat2, long2))


def search_tourist_spots_in_radius(distance, address, city, state, lat, long):
    """
    Search for tourist spots in the distance specified in the parameter.
    :param distance: FLOAT - EXCLUSIVE(for search 5km, pass 6 in parameter)
    :param address: STRING
    :param city: STRING
    :param state: STRING
    :param lat: STRING
    :param long: STRING
    :return: A list of objects of the type Tourist Spots
    """
    if not distance or (not address and (not lat or not long)):
        raise Exception('Wrong parameters')

    list_spots = []

    if address: # Checks if there is at least the address

        api_key = config('GOOGLE_MAPS_KEY', None)

        # Validates the existence of the google key
        if api_key:
            # Make the request in the Google Maps API to obtain the latitude and longitude of the address
            g = geocoder.google(address + ', ' + str(city) + ', ' + str(state), key=api_key)

            if g.json:
                v_lat = g.json['lat']
                v_long = g.json['lng']

                tourist_spots = TbTouristSpot.objects.filter(lat__isnull=False, long__isnull=False)

                # iterates over the list of tourist spots that have latitude and longitude registered
                for reg in tourist_spots:
                    print(reg)
                    v_distance = calculate_distance_great_circle_in_km(v_lat, v_long, reg.lat, reg.long)
                    list_spots.append(reg) if v_distance < distance else None
                return list_spots
            else:
                raise Exception('Address not found')
        else:
            raise Exception('Google API not exists')

    if lat and long:
        tourist_spots = TbTouristSpot.objects.filter(Q(lat__isnull=False) & Q(long__isnull=False))

        # iterates over the list of tourist spots that have latitude and longitude registered
        for reg in tourist_spots:
            v_distance = calculate_distance_great_circle_in_km(lat, long, reg.lat, reg.long)
            list_spots.append(reg) if v_distance < distance else None
        return list_spots
