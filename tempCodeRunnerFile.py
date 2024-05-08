import requests

API_KEY = "9be55026a43edf472a7ee8c016d3de62"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("enter a city name: ")
requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}" 
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    
    print("weather in " + city + " is " + str(temperature) + " degree celciulus")
else:
    print("An error occured")