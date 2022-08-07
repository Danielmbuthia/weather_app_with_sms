import requests
from dotenv import dotenv_values

config = dotenv_values()

WEATHER_API_KEY = config.get('WEATHER_API_KEY')
MY_LAT = config.get('MY_LAT')
MY_LONG = config.get('MY_LONG')
WEATHER_URL = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": WEATHER_API_KEY,
    "exclude": "current,daily,minutely"
}


def get_weather_forcast():
    response = requests.get(url=WEATHER_URL, params=parameters)
    response.raise_for_status()
    data = response.json()
    hourly_data = data['hourly'][:12]
    print(hourly_data)
    data = [weather for weather in hourly_data for weather_id in weather['weather'] if weather_id['id'] < 700]
    if len(data) > 0:
        print("Bring an umbra")
    else:
        print("No need of an umbra")


get_weather_forcast()
