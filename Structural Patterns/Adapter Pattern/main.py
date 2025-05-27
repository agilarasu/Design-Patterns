# Use a legacy/ incompatible Class with a wrapper Class

class FahrenheitWeather:
    def get_weather(self):
        return 86


class CelciusAdapter:
    def __init__(self, weather):
        self.weather = weather

    def get_weather(self):
        f = self.weather.get_weather()
        return round((f - 32) * 5 / 9, 2)


weather_service = FahrenheitWeather()
adapter = CelciusAdapter(weather_service)

print("Temperature in Celsius:", adapter.get_weather())  # Output: 30.0
