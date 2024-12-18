from  .database import get_db, engine
from .models import Base, Lista

def init_db():
    Base.metadata.create_all(bind=engine)

def devolver_mensaje_principal():
    return {"message": "Bienvenido"}

def devolver_listas():
    db = next(get_db())
    listas = db.query(Lista).all()
    return listas

def devolver_lista(id: int):
    db = next(get_db())
    lista_buscada = db.query(Lista).filter(Lista.id == id).first()
    return lista_buscada
