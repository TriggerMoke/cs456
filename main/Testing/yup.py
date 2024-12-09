import math
from geopy.distance import geodesic

# Function for Haversine distance calculation
def haversine(lat1, lon1, lat2, lon2, earth_radius):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return earth_radius * c

# Function for Cosine distance calculation
def cosine(lat1, lon1, lat2, lon2, earth_radius):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    cos_theta = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2)
    return earth_radius * math.acos(cos_theta)

# Function for Vincenty distance calculation using geopy
def vincenty(lat1, lon1, lat2, lon2):
    return geodesic((lat1, lon1), (lat2, lon2)).kilometers  # Note that geopy's geodesic is close to Vincenty

# Load the JSON request
request = {
    "requestType": "distances",
    "places": [
        {"name": "Fort Collins, Colorado", "latitude": 40.52509767120955, "longitude": -105.06983140217429},
        {"name": "Rome, Italy", "latitude": 41.90305264771538, "longitude": 12.466355130870177},
        {"name": "Vila Regina, Argentina", "latitude": -39.098737346397584, "longitude": -67.08541124511255},
        {"name": "Norfolk Island", "latitude": -29.032186550359754, "longitude": 167.94708683534546}
    ],
    "earthRadius": 28980
}

# Calculate distances
earth_radius = request['earthRadius']
places = request['places']

print("Distance Matrix:")
for i in range(len(places)):
    for j in range(i + 1, len(places)):
        lat1, lon1 = places[i]['latitude'], places[i]['longitude']
        lat2, lon2 = places[j]['latitude'], places[j]['longitude']
        
        haversine_distance = haversine(lat1, lon1, lat2, lon2, earth_radius)
        cosine_distance = cosine(lat1, lon1, lat2, lon2, earth_radius)
        vincenty_distance = vincenty(lat1, lon1, lat2, lon2)

        print(f"Between {places[i]['name']} and {places[j]['name']}:")
        print(f"Haversine Distance: {haversine_distance:.2f} units")
        print(f"Cosine Distance: {cosine_distance:.2f} units")
        print(f"Vincenty Distance: {vincenty_distance:.2f} km\n")
