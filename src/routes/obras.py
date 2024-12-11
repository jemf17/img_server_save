from fastapi import APIRouter, UploadFile, File, Path, Body
from src.models.ObraModel import ObraModel
from uuid import UUID
from typing import List

obraRoute = APIRouter(prefix="/obra", tags=['obra'], responses={404: {"description": "Not found"}})

@obraRoute.post("/addobra")
async def add_obra(id_obra: UUID = Body(...), portada: UploadFile = File(...), paginas: List[UploadFile] = File(...)):
    return ObraModel.add(id_obra, paginas, portada)

@obraRoute.get("/{obra_id}/{pag}")
async def get_obra(obra_id: UUID = Path(...), pag: str = Path(...)):
    print('route', pag)
    return ObraModel.get(obra_id, pag)

@obraRoute.get("/{obra_id}")
async def get_portada(obra_id: UUID = Path(...)):
    print(obra_id)
    return ObraModel.getPortada(obra_id)

@obraRoute.put("/{obra_id}")
async def update_obra(obra_id: UUID = Path(...), image: UploadFile = File(...), titulo: str = Body(...)):
    pass

@obraRoute.delete("/{obra_id}")
async def delete_obra(obra_id: UUID):
    pass