import requests
import json
from datetime import datetime
import pytz

api_key = '<YOUR_API_KEY>' # # Replace with your own API key
base_url = "http://api.weatherapi.com/v1"

# For current weather
extension = '/current.json'

place = input("Enter country name: ") # Ask the user to enter a location


# Send a GET request to the WeatherAPI with the user's API key and location
r = requests.get(f"{base_url}{extension}?key={api_key}&q={place}")


# Write the response from the WeatherAPI to a JSON file named after the user's location
with open(f"{place}.json", "w") as f:
    json.dump(r.json(), f, indent=4, sort_keys=True)

# Open the JSON file in read mode and load its contents into a variable
j = open(f"{place}.json", "r")
data = json.load(j)
j.close()

# Get the current time in the user's location using the pytz library
time_obj = datetime.now(pytz.timezone(data['location']['tz_id']))
hours = int(time_obj.strftime('%I'))

# Output the current time and temperature for the user's location

print(f"The localtime in {data['location']['tz_id']} is: ", time_obj.strftime('%Y/%m/%d %I:%M:%S'),  "AM" if hours<12 else "PM")

print(f"The temperature in {place} is: {data['current']['temp_c']} ℃  or  {data['current']['temp_f']} ℉ ")