import requests
import os
from dotenv import load_dotenv

load_dotenv() 

BASE = "http://" + os.environ.get("IPV4_ADDRESS_OF_PI") + ":" + os.environ.get("PORT")

#response = requests.post(BASE + "/wipe", json={"red": 81, "green": 150, "blue": 100})
#print(response.json())

#response = requests.post(BASE + "/theaterChase/randomize")
#print(response.json())

#response = requests.post(BASE + "/theaterChaseRainbow")
#print(response.json())

#response = requests.post(BASE + "/wipe/randomize")
#print(response.json())

response = requests.post(BASE + "/rainbow", json={})
print(response.json())

response = requests.post(BASE + "/comet", json={})
print(response.json())

#response = requests.post(BASE + "/clear", json={})
#print(response.json())