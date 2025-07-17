from pydantic import BaseModel
from datetime import datetime

class AQMSDataCreate(BaseModel):
    temperature: float
    humidity: float
    pm1: float
    pm2_5: float
    pm10: float

class AQMSDataResponse(AQMSDataCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
