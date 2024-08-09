from fastapi import APIRouter
from api.models.cityModel import city
from dotenv import load_dotenv
import os
import requests

weather_api = APIRouter(prefix="/api",tags=["weather"])

load_dotenv()
api_key=os.getenv("api_key")
base_url = os.getenv("base_url")

@weather_api.get("/{name}")
def get_weather(name : str):
    params ={
        "q": name,
        "appid":api_key,
        "units":"metric"
    }
    res = requests.get(base_url,params=params)
    data = res.json()
    return {
        "City": data["name"],
        "Longitude" : data["coord"]["lon"],
        "Latitude " : data["coord"]["lat"],
        "Weather":data["weather"][0]["description"],
        "Temperature": str(data["main"]["temp"])+' %',
        "Humidity" : data['main']["humidity"],
    }