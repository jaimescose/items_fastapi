import models
import schemas
from dependencies import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={404: {'description': 'Not found'}}
)


items = {
    'table': {
        'name': 'table',
        'description': 'wood table',
        'price': 30,
        'units': 15
    },
    'chair': {
        'name': 'chair',
        'description': 'wood chair',
        'price': 15,
        'units': 50
    }
}


@router.get('/', response_model=List[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return models.Item.get_items(db, skip, limit)
