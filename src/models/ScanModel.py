from uuid import UUID
import os
from dotenv import load_dotenv
import shutil
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi import HTTPException

class ScanModel():
    @classmethod
    def add(self,id_obra: UUID, scan: UUID, pages):
        try:
            load_dotenv()
            scan_rute = os.getenv('SCAN_RUTE')
            scan_folder = Path(scan_rute) / str(id_obra)
            scan_folder.mkdir(parents=True, exist_ok=True)
            scan_folder = Path(scan_folder) / str(scan)
            if os.path.exists(scan_folder) and os.path.isdir(scan_folder):
                raise HTTPException(status_code=404, detail="obra traducida por scan ya existente")
            scan_folder.mkdir(parents=True, exist_ok=True)
            pages_url = []
            for pagee in pages:
                pages_url.append(f"scan/{id_obra}/{scan}/{pagee.filename}")
                pagee_location = scan_folder / pagee.filename
                with pagee_location.open("wb") as buffer:
                    shutil.copyfileobj(pagee.file, buffer)
            return {'pagees_scan': pages_url}
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    def update(self,id_obra: UUID,scan: UUID, newpages, oldpages):
        try:
            url_newp = []
            if len(newpages) != len(oldpages):
                raise HTTPException(status_code=404, detail="Los arrays no tienen la misma longitud")
            load_dotenv()
            scan_rute = os.getenv('SCAN_RUTE')
            scan_folder = Path(scan_rute) / str(id_obra) / str(scan)
            for i in range(len(newpages)):
                #agrega
                url_newp.append(f"scan/{id_obra}/{newpages[i].filename}")
                pagee_location = scan_folder / newpages[i].filename
                with pagee_location.open("wb") as buffer:
                    shutil.copyfileobj(newpages[i].file, buffer)
                #elimina
                old_pagee_location = scan_folder / oldpages[i]
                if old_pagee_location.exists():
                    old_pagee_location.unlink()
            return {'newpages': url_newp}
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    def delete(self, id_obra: UUID, scan: UUID):
        try:
            load_dotenv()
            scan_rute = os.getenv('SCAN_RUTE')
            scan_folder = Path(scan_rute) / str(id_obra) / str(scan)
            shutil.rmtree(scan_folder)
            print(scan_folder)
            return {"message": "deleted obra scan"}
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
    @classmethod
    def get(self, id_obra: UUID, scan: UUID, page: str):
        try:
            print("hola")
            load_dotenv()
            scan_rute = os.getenv('SCAN_RUTE')
            scan_img = Path(f"{scan_rute}/{id_obra}/{scan}")
            print(scan_img)
            for root,_,files in os.walk(scan_img):
                #print(files , page)
                
                if page in files:
                    file_path = os.path.join(root, page)
                    return FileResponse(file_path)#, media_type="application/octet-stream") #esta opcion lo que hace es que lo pone para descargar
            raise HTTPException(status_code=404, detail="File not found")
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return None
        
