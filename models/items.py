from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float

from database import Base
from schemas import items


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)

    @classmethod
    def create_item(cls, db: Session, item: items.ItemCreate):
        db_item = cls(name=item.name, description=item.description, price=item.price)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @classmethod
    def get_items(cls, db: Session, skip: int = 0, limit: int = 100):
        return db.query(cls).offset(skip).limit(limit).all()
