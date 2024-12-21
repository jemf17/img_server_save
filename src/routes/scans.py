from fastapi import APIRouter, UploadFile, File, Path, Body
from src.models.ScanModel import ScanModel
from uuid import UUID
from typing import List

scanRoute = APIRouter(prefix="/scan", tags=['scan'], responses={404: {"description": "Not found"}})

@scanRoute.post("/addscan")
async def add_obra(pages: List[UploadFile] = File(...), id_obra: UUID = Body(...), id_scan: UUID = Body(...)):
    return ScanModel.add(id_obra, id_scan,pages)

@scanRoute.get("/{id_obra}/{id_scan}/{page}")
async def get_obras_scab(id_obra: UUID = Path(...),id_scan: UUID = Path(...), page: str = Path(...)):
    print(id_scan)
    return ScanModel.get(id_obra, id_scan, page)

@scanRoute.put("/{id_obra}/{id_scan}")
async def update_obra(id_scan: UUID = Path(...), newpages: List[UploadFile] = File(...), oldpages: List[str]= Body(...), id_obra: UUID = Path(...)):
    if len(oldpages) == 1:
        oldpages = oldpages[0].split(",")
    return ScanModel.update(id_obra, id_scan, newpages, oldpages)

@scanRoute.delete("/{id_obra}/{id_scan}")
async def delete_obra(id_scan: UUID= Path(...),id_obra: UUID = Path(...)):
    return ScanModel.delete(id_obra,id_scan)