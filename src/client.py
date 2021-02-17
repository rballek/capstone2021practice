import requests

response = requests.get("/")
response.raise_for_status()
