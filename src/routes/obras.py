from fastapi import APIRouter, UploadFile, File, Path, Body
from src.models import ImageModel
from uuid import UUID
from typing import List

obraRoute = APIRouter(prefix="/obra", tags=['obra'], responses={404: {"description": "Not found"}})

@obraRoute.post("/addobra")
async def add_obra(id_obra: UUID = Body(...), portada: UploadFile = File(...), paginas: List[UploadFile] = File(...)):
    pass

@obraRoute.get("/{obra_id}")
async def get_obra(obra_id: UUID = Path(...)):
    pass

@obraRoute.get("/portada/{obra_id}")
async def get_portada(obra_id: UUID = Path(...)):
    pass

@obraRoute.put("/{obra_id}")
async def update_obra(obra_id: UUID = Path(...), image: UploadFile = File(...), titulo: str = Body(...)):
    pass

@obraRoute.delete("/{obra_id}")
async def delete_obra(obra_id: UUID):
    pass