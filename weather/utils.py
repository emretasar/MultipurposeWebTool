import requests
from .local_settings import WHEATHER_API_KEY, WHEATHER_API_URL


def get_weather_info(latitude, longtitude):
    request_url = WHEATHER_API_URL.format(lat=latitude, lon=longtitude, api_key=WHEATHER_API_KEY)
    response = requests.get(request_url)
    data = response.json()
        
    datetime_text = data["list"][0]["dt_txt"]
    temprature    = data["list"][0]["main"]["temp"]
    humidity      = data["list"][0]["main"]["humidity"]
    condition     = data["list"][0]["weather"][0]["main"]
    info     = f"Temprature: {temprature}\nHumidity: {humidity}\nTime: {datetime_text}"

    return condition, info