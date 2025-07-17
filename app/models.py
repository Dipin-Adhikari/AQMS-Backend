from sqlalchemy import Column, Integer, Float, DateTime
from .database import Base
from datetime import datetime

class AQMSData(Base):
    __tablename__ = "aqms_data"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float)
    humidity = Column(Float)
    pm1 = Column(Float)
    pm2_5 = Column(Float)
    pm10 = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
