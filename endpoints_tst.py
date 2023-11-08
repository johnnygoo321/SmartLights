import requests

BASE = "http://127.0.0.1:5000"

# response = requests.post(BASE + "/wipe", {"red": 81, "green": 150, "blue": 100})
# print(response.json())

# response = requests.post(BASE + "/randomize")
# print(response.json())

response = requests.post(BASE + "/rainbow")
print(response.json())