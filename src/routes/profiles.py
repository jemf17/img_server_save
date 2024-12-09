from fastapi import APIRouter, UploadFile, File, Path, Body
from uuid import UUID
from src.models.ProfileModel import ProfileModel 

profileRoute = APIRouter(prefix="/profile", tags=['profile'], responses={404: {"description": "Not found"}})

@profileRoute.get("/{user_id}")
async def get_user_profile(user_id: UUID = Path(...)):
    return ProfileModel().get(user_id)

@profileRoute.put("/{user_id}")
async def update_user_profile(user_id: UUID = Path(...), image: UploadFile = File(...)):
    ruta = ProfileModel().update(user_id, image)
    return ruta

@profileRoute.delete("/{user_id})")
async def delete_user_profile(user_id: UUID):
    ProfileModel.delete(user_id)
    return {'image': 'https://jrncdfurtprtrnkiheyq.supabase.co/storage/v1/object/public/profils/img_profiles/profile.jpg'}

@profileRoute.post("/addprofile")
async def add_friend_to_user(image: UploadFile = File(...), id_user: UUID = Body(...)):
    ruta = ProfileModel().add(id_user, image)
    return {'image': ruta}