from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from supermarketlist import SupermarketList
from supermarketlist.models import Lista
from supermarketlist.schemas import Lista as ListaSchema
from supermarketlist.schemas import Item as ItemSchema
from logging_config import logger

SupermarketList.init_db()

app = FastAPI()

@app.get("/favicon.ico")
async def read_favicon():
    return FileResponse("./favicon.ico")

@app.get("/")
async def read_root():
    logger.info("Bienvenida")
    return SupermarketList.devolver_mensaje_principal()

@app.get("/listas")
async def read_listas():
    logger.info("Devolviendo lista de listas")
    return SupermarketList.devolver_listas()

@app.post("/listas")
async def create_lista(lista: ListaSchema):
    logger.info("Creando una nueva lista")
    SupermarketList.crear_lista(lista)
    return HTTPException(status_code=200, detail="Lista creada")

@app.get("/listas/{id}")
async def read_lista(id: int):
    lista_buscada = SupermarketList.devolver_lista(id)
    
    if lista_buscada is None:
        logger.error("No se encontró la lista con id: %s", id)
        raise HTTPException(status_code=404, detail="Lista no encontrada")
    
    logger.info("Devolviendo la lista con id: %s", id)
    return lista_buscada

@app.post("/listas/{lista_id}/items")
async def create_item(lista_id: int, item: ItemSchema):
    logger.info("Creando nuevo item en lista: %s", lista_id)
    SupermarketList.agregar_item(lista_id, item)
    return HTTPException(status_code=200, detail="Item agregado")

