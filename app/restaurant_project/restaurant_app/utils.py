import requests

def get_weather(api_key, lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp_k = data["main"]["temp"]
        temp_f = (temp_k - 273.15) * 9/5 + 32  # Convert Kelvin to Fahrenheit
        weather = data["weather"][0]["main"]
        return {"temp": temp_f, "weather": weather}
    else:
        raise Exception(f"Failed to fetch weather data: {response.text}")
