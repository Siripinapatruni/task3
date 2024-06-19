import requests

def fetch_weather(api_key, location):
    """Fetch current weather data from OpenWeatherMap API."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use metric units (celcius)
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as err:
        print(f"Error fetching data: {err}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"Connection error: {err}")
        return None

def display_weather(weather_data):
    """Display weather information."""
    if weather_data is not None:
        city = weather_data['name']
        country = weather_data['sys']['country']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("No weather data to display.")

def main():
    print("Welcome to the Weather App!")
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    location = input("Enter the city name or ZIP code: ").strip()

    # Fetch weather data
    weather_data = fetch_weather(api_key, location)

    # Display weather information
    display_weather(weather_data)

if __name__ == "__main__":
    main()
