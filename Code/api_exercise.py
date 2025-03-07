import requests
import json

def get_weather_forecast(api_key, location):
    """
    Make a GET request to the /forecast endpoint to fetch the weather forecast for the next 3 days.

    Args:
        api_key (str): Your WeatherAPI key.
        location (str): The location for which you want to fetch the weather forecast (e.g., "New York").

    Returns:
        dict: A dictionary containing the weather forecast data.
    """
    base_url = "http://api.weatherapi.com/v1/forecast.json"
    params = {
        "key": api_key,
        "q": location,
        "days": 3
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def extract_and_display_forecast(forecast_data):
    """
    Extract and display the date, average temperature, and weather condition for each of the 3 days.

    Args:
        forecast_data (dict): A dictionary containing the weather forecast data.
    """
    if forecast_data is None:
        return

    forecast = forecast_data["forecast"]["forecastday"]
    for day in forecast:
        date = day["date"]
        avg_temp = day["day"]["avgtemp_c"]
        condition = day["day"]["condition"]["text"]
        print(f"Date: {date}")
        print(f"Average Temperature: {avg_temp}°C")
        print(f"Weather Condition: {condition}")
        print("------------------------")

def get_location():
    """
    Get the location from the user and validate it.

    Returns:
        str: The validated location.
    """
    api_key = '9c22d1d65d8844d19e5131751252801'
    while True:
        location = input("Please enter a location: ")
        forecast_data = get_weather_forecast(api_key, location)
        if forecast_data is not None and "forecast" in forecast_data and "forecastday" in forecast_data["forecast"]:
            return location
        else:
            print("Invalid location. Please try again .")

def main():
    location = get_location()
    api_key = '9c22d1d65d8844d19e5131751252801'
    forecast_data = get_weather_forecast(api_key, location)
    extract_and_display_forecast(forecast_data)

if __name__ == "__main__":
    main()