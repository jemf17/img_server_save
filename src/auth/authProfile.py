from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv


def verify_profile_user(token:  str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    # verificar que en verdad el usuario es en verdad el que dice ser
    # se tiene que mandar un token con ese mismo uuid de usuario, al decepcriptarlo tiene que ser el mismo uuid que se mando 
    # como parametro uuid

    # 2 3 6 => [2,3,6] => [img2, img3, img6] => [strimg2, strimg3, strimg6]
    
    pass