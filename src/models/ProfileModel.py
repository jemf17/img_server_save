from fastapi import HTTPException
from uuid import UUID
import os
from dotenv import load_dotenv
import shutil
from fastapi.responses import FileResponse
from pathlib import Path
class ProfileModel():
    @classmethod
    def add(self, user_id: UUID, image):
        try:
            load_dotenv()
            profile_rute = os.getenv('PROFILE_RUTE')
            user_folder = Path(profile_rute) / str(user_id)
            user_folder.mkdir(parents=True, exist_ok=True)
            file_location = user_folder / image.filename
            url_img  = f'''profile/{user_id}'''
            files = [f for f in user_folder.iterdir() if f.is_file()]
            if len(files) >= 1:
                raise HTTPException('Profile already exists')
            # Guardar la imagen en el directorio del usuario
            with file_location.open("wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            return {'message' : url_img}
        except Exception as e:
            print(f"Error adding new profile: {e}")
            return {"success": False, "error": str(e)}
    @classmethod
    def update(self, user_id: UUID, image):
        try:
            load_dotenv()
            profile_rute = os.getenv('PROFILE_RUTE')
            user_folder = Path(profile_rute) / str(user_id)
            #limpia el directorio del usuario
            print("directorio",user_folder)
            for file in user_folder.iterdir():
                file.unlink()
            file_location = user_folder / image.filename
            with file_location.open("wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            return file_location
        except Exception as e:
            return {"success": False, "error": str(e)}
    @classmethod
    def delete(self, user_id: UUID):
        try:
            user_folder = Path(f"""save/profile/{user_id}""")
            #limpia el directorio del usuario
            for file in user_folder.iterdir():
                file.unlink()
            print("Deleting profile")
        except Exception as e:
            return {"success": False, "error": str(e)}
    @classmethod
    def get(self, user_id: UUID):
        try:
            IMAGE_DIRECTORY = Path(f"""save/profile/{user_id}""")
            image_files = list(IMAGE_DIRECTORY.glob("*"))
            if not image_files:
                raise HTTPException(status_code=404, detail="No hay imágenes en el directorio")
            #if len(image_files) > 1:
            #    raise HTTPException(status_code=500, detail="Hay más de una imagen en el directorio")
            return FileResponse(image_files[0])
        except Exception as e:
            return {"success": False, "error": str(e)}