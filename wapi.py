from math import floor
from urllib import response
from geopy.geocoders import Nominatim
import requests
import json
# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("Sun City")

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)

# floor
url = f'https://api.openweathermap.org/data/2.5/weather?q=Sun City&units=imperial&appid=396b8dda92a5079f3bbf2704d32fc382'

res = requests.get(url)
print(res)
data = json.loads(res.text)

with open('weather-data.json', 'w+') as f:
    f.write(res.text)
    f.close()

print(
    f'It feels like: {data["main"]["feels_like"]} {data["weather"][0]["icon"]}')
