from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Разрешаем запросы с любого источника (для теста)
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

class RouteResponse(BaseModel):
    status: str
    path: List[List[float]]
    distance: float = 1.23
    duration: float = 6.0
    price: float = 1000.0

class OrderRequest(BaseModel):
    from_: str
    to: str
    tariff: str
    distance_m: float
    price: float

@app.post("/api/v1/calculate-route", response_model=RouteResponse)
def calculate_route(req: RouteRequest):
    # Возвращаем фиктивный маршрут (две точки: старт и финиш)
    return RouteResponse(
        status="Success",
        path=[[req.start_lat, req.start_lng], [req.end_lat, req.end_lng]],
        distance=1.23,
        duration=6.0,
        price=1000.0
    )

@app.post("/api/v1/submit-order")
def submit_order(req: OrderRequest):
    # Просто подтверждаем приём заказа
    return {"status": "Order received"} 