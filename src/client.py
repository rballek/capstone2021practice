import requests

#using response library to raise status one endpoint
response = requests.get("/")
response.raise_for_status()
