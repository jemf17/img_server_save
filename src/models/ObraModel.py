from uuid import UUID
import os
from dotenv import load_dotenv
import shutil
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi import HTTPException
class ObraModel():
    @classmethod
    def add(self, id_obra: UUID, pags, portada, textnt):
        try:
            print(type(id_obra), type(pags), type(portada), type(textnt))
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
            if len(textnt) != 0:
                pass
            return {'portada': port_location, 'pages': pags_url}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @classmethod
    def delete(self, id_obra: UUID):
        try:
            load_dotenv()
            rute = os.getenv('OBRA_RUTE')
            obra_folder = Path(rute) / str(id_obra)
            shutil.rmtree(obra_folder)
            return {"message": "obra deleted"}
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
    def updatePortada(self, id_obra: UUID, image):
        try:
            load_dotenv()
            obra_rute = os.getenv('OBRA_RUTE')
            obra_folder = Path(obra_rute) / str(id_obra) / 'portada'
            #limpia el directorio del usuario
            print("directorio",obra_folder)
            for file in obra_folder.iterdir():
                file.unlink()
            file_location = obra_folder / image.filename
            with file_location.open("wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            return {"success": True, "message": 'Ok'}
        except Exception as e:
            return {"success": False, "error": str(e)}
    @classmethod
    def update(self, id_obra: UUID, newpags, oldpags):
        try:
            # primero se determina la obra a actualizar con el id_obra
            # luego se resive las nuevas paginas y las viejas paginas, pero solamente el nombre de las mismas para identificarlas
            # se busca esa obra, se elimina y despues se agrega la imagen de la lista de newpags
            # asi iterativamente y se retorna una lista con las nuevas rutas de las paginas editadas
            # en el front se debera identificar el numero de pagina de cada pag editada y ese mismo orden tendra que tener 
            # las nuevas y viejas pags ej: [2,4,5] -> [newp2,newp4,newp5] y [oldp2,oldp4,oldp5]
            url_newp = []
            if len(newpags) != len(oldpags):
                raise HTTPException(status_code=404, detail="Los arrays no tienen la misma longitud")
            load_dotenv()
            obra_rute = os.getenv('OBRA_RUTE')
            pages_folder = Path(obra_rute) / str(id_obra) / 'pages'
            for i in range(len(newpags)):
                #agrega
                url_newp.append(f"obras/{id_obra}/{newpags[i].filename}")
                page_location = pages_folder / newpags[i].filename
                with page_location.open("wb") as buffer:
                    shutil.copyfileobj(newpags[i].file, buffer)
                #elimina
                old_page_location = pages_folder / oldpags[i]
                if old_page_location.exists():
                    old_page_location.unlink()
            return {'newpags': url_newp}
        except Exception as e:
            return {"success": False, "error": str(e)}