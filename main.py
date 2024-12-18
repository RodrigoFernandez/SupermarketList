from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from supermarketlist import SupermarketList

app = FastAPI()

SupermarketList.init_db()
@app.get("/favicon.ico")
async def read_favicon():
    return FileResponse("./favicon.ico")

@app.get("/")
async def read_root():
    return SupermarketList.devolver_mensaje_principal()

@app.get("/listas")
async def read_listas():
    return SupermarketList.devolver_listas()

@app.get("/listas/{id}")
async def read_lista(id: int):
    lista_buscada = SupermarketList.devolver_lista(id)
    #return lista_buscada if lista_buscada else {"message": "Lista no encontrada"}
    if lista_buscada is None:
        raise HTTPException(status_code=404, detail="Lista no encontrada")
    return lista_buscada



