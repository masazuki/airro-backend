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

@app.post("/api/v1/calculate-route")
def calculate_route(req: RouteRequest):
    return {
        "status": "Success",
        "path": [[req.start_lat, req.start_lng], [req.end_lat, req.end_lng]],
        "distance_m": 1450.0,
        "duration": 510.0,
        "price": 1750.0,
        "predicted_values": {
            "estimated_time_sec": 510,
            "required_battery_percent": 38.5,
            "route_risk_level": 0.07
        },
        "weatherInfo": {
            "description": "Солнечно",
            "wind_speed_mps": 3.2,
            "is_rain": False
        },
        "warnings": ["Возможны порывы ветра на высоте"]
    }

@app.post("/api/v1/submit-order")
def submit_order(req: OrderRequest):
    return {"status": "Order received"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
