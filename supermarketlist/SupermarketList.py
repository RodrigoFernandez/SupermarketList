from  .database import get_db, engine
from sqlalchemy.orm import joinedload
from .models import Base, Lista, Item
from .schemas import Lista as ListaSchema, Item as ItemSchema

def init_db():
    Base.metadata.create_all(bind=engine)

def devolver_mensaje_principal():
    return {"message": "Bienvenido"}

def devolver_listas():
    db = next(get_db())
    listas = db.query(Lista).all()
    return listas

def crear_lista(lista: ListaSchema):
    db = next(get_db())
    db_lista = Lista(nombre=lista.nombre)
    db_lista.items = lista.items
    db.add(db_lista)
    db.commit()
    db.refresh(db_lista)
    return db_lista

def devolver_lista(id: int):
    db = next(get_db())
    lista_buscada = db.query(Lista).options(joinedload(Lista.items)).filter(Lista.id == id).first()
    return lista_buscada

def agregar_item(lista_id: int, item: ItemSchema):
    db = next(get_db())
    db_item = Item(nombre=item.nombre, cantidad=item.cantidad, comprado=item.comprado, lista_id=lista_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/listas/", response_model=schemas.Lista)
def crear_lista(lista: schemas.ListaCreate, db: Session = Depends(get_db)):
    db_lista = models.Lista(nombre=lista.nombre)
    db.add(db_lista)
    db.commit()
    db.refresh(db_lista)
    return db_lista

@app.get("/listas/", response_model=List[schemas.Lista])
def leer_listas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    listas = db.query(models.Lista).offset(skip).limit(limit).all()
    return listas

@app.get("/listas/{lista_id}", response_model=schemas.Lista)
def leer_lista(lista_id: int, db: Session = Depends(get_db)):
    lista = db.query(models.Lista).filter(models.Lista.id == lista_id).first()
    if lista is None:
        raise HTTPException(status_code=404, detail="Lista no encontrada")
    return lista

@app.post("/listas/{lista_id}/items/", response_model=schemas.Item)
def crear_item(lista_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    lista = db.query(models.Lista).filter(models.Lista.id == lista_id).first()
    if lista is None:
        raise HTTPException(status_code=404, detail="Lista no encontrada")
    db_item = models.Item(**item.dict(), lista_id=lista_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.put("/items/{item_id}", response_model=schemas.Item)
def actualizar_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

y mirar como se usa Pydantic
"""