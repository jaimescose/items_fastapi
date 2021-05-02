import database
import models
from database import SessionLocal, engine
from fastapi import FastAPI
from routers import items

database.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(items.router)
