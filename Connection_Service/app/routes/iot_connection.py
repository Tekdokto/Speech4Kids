from fastapi import APIRouter
from app.services.wifi_connector import WiFiConnector

router = APIRouter()

@router.post("/wifi/connect")
async def connect_to_wifi(ssid: str, password: str):
    connector = WiFiConnector(ssid, password)
    connector.connect()
    return {"message": f"Connected to Wi-Fi network: {ssid}"}
