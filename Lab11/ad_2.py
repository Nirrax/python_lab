import json

import requests


def get_weather():
    url = "https://worldweather.wmo.int/pl/json/2167_pl.xml"
    response = requests.get(url)
    data = response.json()
    return data["city"]["forecast"]


def get_max_and_min_temperature(weather_data: dict):
    result = []
    weather_data = weather_data["forecastDay"][:3]
    for day in weather_data:
        result.append(
            {
                "date": day["forecastDate"],
                "max_temp": day["maxTemp"],
                "min_temp": day["minTemp"],
            }
        )
    return result


def save_weather_data(weather_data: list, filepath: str):
    with open(filepath, "w") as file:
        json.dump(weather_data, file)


data = get_max_and_min_temperature(get_weather())
save_weather_data(data, "weather_data.json")
