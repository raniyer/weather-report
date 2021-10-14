import pyowm
from datetime import datetime
from api_key import API_KEY
from timezone_conversion import gmt_to_calcutta

owm = pyowm.OWM(API_KEY)
mgr = owm.weather_manager()
place = "New York, US"

def get_temprature():
    days = []
    dates = []
    temp_min = []
    temp_max = []

    caster = mgr.forecast_at_place(place, '3h')
    forecast = caster.forecast
    for weather in forecast:
        day = gmt_to_calcutta(weather.reference_time())
        date = day.date()
        if date not in dates:
            dates.append(date)
            temp_max.append(None)
            temp_min.append(None)
            days.append(date)
        temprature = weather.temperature('fahrenheit')['temp']
        if not temp_min[-1] or temprature < temp_min[-1]:
            temp_min[-1] = temprature
        if not temp_max[-1] or temprature > temp_max[-1]:
            temp_max[-1] = temprature
    print(days, temp_min, temp_max)
    return(days, temp_min, temp_max)

if __name__ == '__main__':
    get_temprature()        

