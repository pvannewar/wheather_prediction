from django.shortcuts import render
from .utils import get_weather

def index(request):
    # Render the index.html template
    return render(request, "index.html")
def results(request):
    # Replace with your actual API key
    api_key = "cb23456fa2471b70a37ce771e929db92"
    lat = 40.768
    lon = -73.525

    # Call get_weather with all required arguments
    weather_data = get_weather(api_key=api_key, lat=lat, lon=lon)

    context = {
        "weather_data": weather_data,
    }
    return render(request, "results.html", context)
