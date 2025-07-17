from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, db: Session = Depends(get_db)):
    data = crud.get_all_data(db)
    return templates.TemplateResponse("index.html", {"request": request, "data": data})

@app.post("/upload", response_model=schemas.AQMSDataResponse)
def upload_data(data: schemas.AQMSDataCreate, db: Session = Depends(get_db)):
    return crud.create_aqms_data(db, data)
