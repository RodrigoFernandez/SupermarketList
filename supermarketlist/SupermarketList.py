listas = [
    {"id": 0, "nombre": "Lista 1", "items": [{"id": 0, "nombre": "Item 1", "cantidad": 1},
                                                         {"id": 1, "nombre": "Item 2", "cantidad": 2}]},
    {"id": 1, "nombre": "Lista 2", "items": [{"id": 0, "nombre": "Item 1", "cantidad": 1},
                                                         {"id": 1, "nombre": "Item 2", "cantidad": 3}]},
            ]

def devolver_mensaje_principal():
    return {"message": "Bienvenido"}

def devolver_listas():
    return {"message": "Listas",
            "listas": [{"id": l.get("id"), "nombre": l.get("nombre")} for l in listas]}

def devolver_lista(id: int):
    lista_buscada = listas[id]
    return {"message": f"Lista {lista_buscada.get('nombre')}",
            "lista": lista_buscada}
