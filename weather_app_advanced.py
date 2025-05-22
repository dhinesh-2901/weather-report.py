import requests
api = "97ca08c69c87f7aedff7821221853929" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": api,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        return None  # Return None if city is not found

# Example usage
city_name = input("Enter city name: ")
weather_data = get_weather(city_name)

if weather_data:
    print(f"Weather in {weather_data['city']}:")
    print(f"🌡️ Temperature: {weather_data['temperature']}°C")
    print(f"🌤️ Condition: {weather_data['weather'].title()}")
    print(f"💧 Humidity: {weather_data['humidity']}%")
    print(f"🌬️ Wind Speed: {weather_data['wind_speed']} m/s")
else:
    print("❌ City not found. Please try again.")