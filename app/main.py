from fastapi import FastAPI
from api.routes.weatherRouter import weather_api

app = FastAPI()
app.include_router(weather_api)

@app.get('/')
def index():
    return {"status":"weather api is running"}