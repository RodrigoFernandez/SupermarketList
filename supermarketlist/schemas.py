"""
Schemas para la API de la lista de compras

Permite la serialización y deserialización de los datos recibidos
"""
from pydantic import BaseModel
from typing import List, Optional

class ItemBase(BaseModel):
    nombre: str
    cantidad: int = 1
    comprado: bool = False

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: Optional[int] = None
    lista_id: Optional[int] = None

    class Config:
        from_attributes = True

class ListaBase(BaseModel):
    nombre: str

class ListaCreate(ListaBase):
    pass

class Lista(ListaBase):
    id: Optional[int] = None
    items: List[Item] = []

    class Config:
        from_attributes = True 