from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import os
import uvicorn

app = FastAPI()

# Разрешаем запросы с любого источника
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RouteRequest(BaseModel):
    start_lat: float
    start_lng: float
    end_lat: float
    end_lng: float

class OrderRequest(BaseModel):
    from_: str
    to: str
    tariff: str
    distance_m: float
    price: float

@app.post("/api/v1/calculate-route", response_model=RouteResponse)
def calculate_route(req: RouteRequest):
    return {
        "status": "Success",
        "path": [[req.start_lat, req.start_lng], [req.end_lat, req.end_lng]],
        "distance": 1450.0,
        "duration": 510.0,
        "price": 1750.0,
        "predictedValues": {
            "estimatedTimeSec": 510,
            "requiredBatteryPercent": 38.5,
            "routeRiskLevel": 0.07
        },
        "weatherInfo": {
            "description": "Солнечно",
            "windSpeedMps": 3.2,
            "isRain": False
        },
        "warnings": ["Возможны порывы ветра на высоте"]
    }
