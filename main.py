import requests

api_key = "OpenWeatherMap Token"


weather_param = {
    "lat": 50.100090,
    "lon": 14.007300,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_param)
response.raise_for_status()
data = response.json()

data_weather = data['list'][0]['weather'][0]['id']
data_id = []

will_rain = False
for data_hour in data['list']:
    weather = data_hour["weather"][0]["id"]
    if int(weather) < 700:
        will_rain = True
if will_rain:
    print("Vem si deštník")
else:
    print("Dneska bude hezky")
