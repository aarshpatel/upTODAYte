from geopy.geocoders import Nominatim

def convert_location_to_lat_lng(location):
	""" Return the lat, lng coordinates of a location """
	geolocator = Nominatim()
	location = geolocator.geocode(location)
	try:
		return (location.latitude, location.longitude)
	except: 
		return None


