import requests
from dotenv import dotenv_values

from sms import Sms

config = dotenv_values()

WEATHER_API_KEY = config.get('WEATHER_API_KEY')
MY_LAT = config.get('MY_LAT')
MY_LONG = config.get('MY_LONG')
TO_NUMBER = config.get("SEND_TO")
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
    data = [weather for weather in hourly_data for weather_id in weather['weather'] if weather_id['id'] < 700]
    # less than 700 means rain or snow
    if len(data) > 0:
        sms = Sms(TO_NUMBER, "Remember to carry an umbrella")
        sms.send()
    return


get_weather_forcast()
