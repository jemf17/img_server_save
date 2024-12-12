from fastapi import APIRouter, UploadFile, File, Path, Body
from src.models.ObraModel import ObraModel
from uuid import UUID
from typing import List

obraRoute = APIRouter(prefix="/obra", tags=['obra'], responses={404: {"description": "Not found"}})
#agrega una obra
@obraRoute.post("/addobra")
async def add_obra(id_obra: UUID = Body(...), portada: UploadFile = File(...), paginas: List[UploadFile] = File(...)):#, pag_textnt: List[UploadFile] = File(...)):
    pag_textnt = []
    return ObraModel.add(id_obra, paginas, portada, pag_textnt)
# retorna la pagina de la obra
@obraRoute.get("/{obra_id}/{pag}")
async def get_obra(obra_id: UUID = Path(...), pag: str = Path(...)):
    return ObraModel.get(obra_id, pag)

#retorna la portada de la obra
@obraRoute.get("/{obra_id}")
async def get_portada(obra_id: UUID = Path(...)):
    print(obra_id)
    return ObraModel.getPortada(obra_id)
#actualiza y retorna los links de las nuevas urls de las pags
@obraRoute.put("/{obra_id}")
async def update_obra(obra_id: UUID = Path(...), newpag: List[UploadFile] = File(...), oldpag: List[str] = Body(...)):
    if len(oldpag) == 1:
        oldpag = oldpag[0].split(",")
    return ObraModel.update(obra_id, newpag, oldpag)
#actualiza la portada
@obraRoute.put("/portada/{obra_id}")
async def update_portada(obra_id: UUID = Path(...), portada: UploadFile = File(...)):
    return ObraModel.updatePortada(obra_id, portada)
#elimina una obra
@obraRoute.delete("/{obra_id}")
async def delete_obra(obra_id: UUID):
    return ObraModel.delete(obra_id)
@obraRoute.put("/textnt/{obra_id}")
async def update_textnt(obra_id: UUID = Path(...), newpag: List[UploadFile] = File(...), oldpag: List[str] = Body(...)):
    pass

@obraRoute.post("/textnt")
async def update_textnt(obra_id: UUID = Path(...), pag: List[UploadFile] = File(...)):
    pass