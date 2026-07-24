import requests
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 28.6139,
    "longitude": 77.2090,

    "current_weather": True
}

response = requests.get(url, params=params)

print("status code:", response.status_code)
data = response.json()

print("/nfull response:")
print(data)

weather = data["current_weather "]
print("/ncurrent weather:")
print("temperature : ", weather["temperature"],"celsius")
print("windspeed : ", weather["windspeed"],"km/h")
print("winddirection : ", weather["winddirection"],"degrees")