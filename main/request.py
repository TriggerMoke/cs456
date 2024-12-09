import requests
import json

# Define the URL
url = "https://black-bottle.cs.colostate.edu:31449/api/distances"

# Define the request payload
data = {
    "requestType": "distances",
    "places": [
        {"name": "Bogotá", "latitude": "4.719339513562428", "longitude": "-73.87465962748392"},
        {"name": "Bulawayo", "latitude": "-20.147195510168142", "longitude": "28.56364538140389"},
        {"name": "Sapporo", "latitude": "43.07320520445964", "longitude": "141.33583321261543"},
        {"name": "Denali", "latitude": "63.654098982402736", "longitude": "-148.71390083242008"}
    ],
    "earthRadius": 1266801.877,
    "formula": "haversine",
    "distances": [2284657.5996, 2654497.7332, 965958.8006, 1748588.2447]
}

# Send the POST request with the JSON data
response = requests.post(url, json=data)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response Content:", response.text)
