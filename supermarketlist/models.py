from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .database import Base

class Lista(Base):
    __tablename__ = "listas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    items = relationship("Item", back_populates="lista")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    cantidad = Column(Integer)
    comprado = Column(Boolean, default=False)
    lista_id = Column(Integer, ForeignKey("listas.id"))
    lista = relationship("Lista", back_populates="items")

