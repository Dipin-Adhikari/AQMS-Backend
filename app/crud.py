from sqlalchemy.orm import Session
from . import models, schemas

def create_aqms_data(db: Session, data: schemas.AQMSDataCreate):
    db_data = models.AQMSData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_all_data(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AQMSData).offset(skip).limit(limit).all()
