import requests
import time

class WeatherChecker:
    def __init__(self, api_key, city_name):
        # Initialize with the provided API key and city name
        self.api_key = api_key
        self.city_name = city_name
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather(self):
        # Retrieve current weather data
        url = self.base_url + "appid=" + self.api_key + "&q=" + self.city_name
        response = requests.get(url)
        return response.json()

    def is_bad_weather(self, weather_data):
        # Check if the current weather is considered bad (severe)
        bad_weather_conditions = ['Rain', 'Snow', 'Hail', 'Sleet', 'Freeze', 'Cold', 'Wind', 'Heat', 'Heavy Rain', 'Continuous Rain']
        if 'weather' in weather_data:
            for weather in weather_data['weather']:
                if weather['main'] in bad_weather_conditions:
                    return True
        return False

    def check_current_severe_weather(self):
        # Check for severe weather at the current time
        weather_data = self.get_weather()
        return self.is_bad_weather(weather_data)

# How to use
api_key = '32b8600ccd902c30801c6fe5ac806afa'
city_name = 'Los Angeles'
weather_checker = WeatherChecker(api_key, city_name)
current_bad_weather = weather_checker.check_current_severe_weather()
if current_bad_weather:
    print("Severe weather is currently present.")
else:
    print("Weather is currently good.")
