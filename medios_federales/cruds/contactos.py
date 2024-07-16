from sqlalchemy.orm import Session
from ..models import contactos as model_contacto

def create_item(db: Session, item: dict):
    db_item = model_contacto.Contactos(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
