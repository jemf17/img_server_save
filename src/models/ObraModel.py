from uuid import UUID
import os
from dotenv import load_dotenv
import shutil
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi import HTTPException
class ObraModel():
    @classmethod
    def add(self, id_obra: UUID, pags, portada):
        try:
            load_dotenv()
            #se define la ruta base
            rute = os.getenv('OBRA_RUTE')
            obra_folder = Path(rute) / str(id_obra)
            if os.path.exists(obra_folder) and os.path.isdir(obra_folder):
                raise HTTPException(status_code=404, detail="Obra ya existente")
            obra_folder.mkdir(parents=True, exist_ok=True)
            #crea los directorios pages y textnt
            os.makedirs(os.path.join(obra_folder, 'pages'), exist_ok=True)
            os.makedirs(os.path.join(obra_folder, 'textnt'), exist_ok=True)
            os.makedirs(os.path.join(obra_folder, 'portada'), exist_ok=True)
            #guarda la portada
            port_location = obra_folder / 'portada' / portada.filename
            with port_location.open("wb") as buffer:
                shutil.copyfileobj(portada.file, buffer)
            #guardar las paginas
            pags_url = []
            pages_folder = obra_folder / 'pages'
            for page in pags:
                pags_url.append(f"obras/{id_obra}/{page.filename}")
                page_location = pages_folder / page.filename
                with page_location.open("wb") as buffer:
                    shutil.copyfileobj(page.file, buffer)
            return {'portada': port_location, 'pages': pags_url}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @classmethod
    def delete(self, id_obra: UUID):
        try:
            pass
        except Exception as e:
            return {"success": False, "error": str(e)}
    @classmethod
    def get(self, id_obra: UUID, pag: str):
        try:
            load_dotenv()
            pag_rute = os.getenv('OBRA_RUTE')
            BASE_DIR = Path(f"{pag_rute}/{id_obra}/pages")
            for root,_,files in os.walk(BASE_DIR):
                print(files , pag)
                if pag in files:
                    file_path = os.path.join(root, pag)
                    return FileResponse(file_path)#, media_type="application/octet-stream") #esta opcion lo que hace es que lo pone para descargar
            raise HTTPException(status_code=404, detail="File not found")
        except Exception as e:
            return {"success": False, "error": str(e)}
    @classmethod
    def getPortada(self, id_obra: UUID):
        try:
            load_dotenv()
            port_rute = os.getenv('OBRA_RUTE')
            BASE_DIR = Path(port_rute) / str(id_obra) / 'portada'
            image_files = list(BASE_DIR.glob("*"))
            print('imagen:',image_files, 'ruta', BASE_DIR)
            if not image_files:
                raise HTTPException(status_code=404, detail="No hay imágenes en el directorio")
            return FileResponse(image_files[0])
        except Exception as e:
            return {"success": False, "error": str(e)}
    @classmethod
    def updatePortada(self, id_obra: UUID):
        try:
            pass
        except Exception as e:
            return {"success": False, "error": str(e)}
    @classmethod
    def update(self, id_obra: UUID, pags, portada):
        try:
            pass
        except Exception as e:
            return {"success": False, "error": str(e)}