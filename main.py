from fastapi import FastAPI, APIRouter
from fastapi.responses import FileResponse
from supermarketlist import SupermarketList


router = APIRouter(prefix="/favicon.ico")

@router.get("/")
async def read_favicon():
    return FileResponse("./favicon.ico")

app = FastAPI()

@app.get("/")
async def read_root():
    return SupermarketList.devolver_mensaje_principal()

@app.get("/listas")
async def read_listas():
    return SupermarketList.devolver_listas()

@app.get("/listas/{id}")
async def read_lista(id: int):
    return SupermarketList.devolver_lista(id)



