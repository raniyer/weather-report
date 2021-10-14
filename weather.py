import pyowm
from api_key import API_KEY

owm = pyowm.OWM(API_KEY)

mgr = owm.weather_manager()
place = 'Patna, IN'
obs = mgr.weather_at_place(place)
weather = obs.weather 
temprature = weather.temperature(unit = 'fahrenheit')['temp']
weather = obs.weather
clouds = weather.clouds
wind = weather.wind('miles_hour')['speed']
print(f"Today's temprature in {place} is {temprature} degrees")
print(f'The current cloud coverage for {place} is {clouds}%.')
print(f'The current wind speed for {place} is {wind}mph.')
print(f"Today's weather for {place}: {weather.status}.")
print(f"Today's detailed weather for {place}: {weather.detailed_status}.")

print(f"Sunrise at {weather.sunrise_time(timeformat='iso')} UTC")
