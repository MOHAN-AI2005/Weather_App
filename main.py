import requests

API_KEY = "your_api_key_here"  # Replace with OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()
    if data.get("main"):
        print(f"{city} - {data['main']['temp']}°C, {data['weather'][0]['description']}")
    else:
        print("City not found.")

while True:
    city = input("Enter city name (or 'exit'): ")
    if city == "exit":
        break
    get_weather(city)
