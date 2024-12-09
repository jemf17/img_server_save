from fastapi import APIRouter, UploadFile, File, Path, Body
from src.models import ImageModel
from uuid import UUID

obraRoute = APIRouter(prefix="/obra", tags=['obra'], responses={404: {"description": "Not found"}})

@obraRoute.post("/addobra")
async def add_obra(image: UploadFile = File(...), titulo: str = Body(...), id_user: UUID = Body(...)):
    pass

@obraRoute.get("/{user_id}")
async def get_obras_user(user_id: UUID = Path(...)):
    pass

@obraRoute.put("/{user_id}")
async def update_obra(user_id: UUID = Path(...), image: UploadFile = File(...), titulo: str = Body(...)):
    pass

@obraRoute.delete("/{user_id}")
async def delete_obra(user_id: UUID):
    pass