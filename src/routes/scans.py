from fastapi import APIRouter, UploadFile, File, Path, Body
from src.models import ImageModel
from uuid import UUID

scanRoute = APIRouter(prefix="/scan", tags=['scan'], responses={404: {"description": "Not found"}})

@scanRoute.post("/addscan")
async def add_obra(image: UploadFile = File(...), titulo: str = Body(...), id_user: UUID = Body(...)):
    pass

@scanRoute.get("/{scan_id}")
async def get_obras_user(user_id: UUID = Path(...)):
    pass

@scanRoute.put("/{user_id}")
async def update_obra(user_id: UUID = Path(...), image: UploadFile = File(...), titulo: str = Body(...)):
    pass

@scanRoute.delete("/{user_id}")
async def delete_obra(user_id: UUID):
    pass