import requests

url = f"http://api.weatherapi.com/v1/current.json?key=151615164565&q=London&days=1"

response  = requests.get(url)

base_url = "http://api.weatherapi.com/v1/"

endpoint_url = f'https://api.weatherapi.com/v1/current.json'

params = f" ? key=151615164565 & q=London & days=1 "

