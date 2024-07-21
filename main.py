import requests
import json
import win32com.client as wincom

city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=7ac3ee0ac4ff4170b2754421241507&q={city}"

r = requests.get(url)
weatherdic = json.loads(r.text)
w = weatherdic["current"]["temp_c"]

speak = wincom.Dispatch("SAPI.SpVoice")
text = (f"The current weather in {city} is {w} degree")
speak.Speak(text)