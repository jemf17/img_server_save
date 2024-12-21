from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

def verify_toker_obra(token:  str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    # se verifica que el usuario existe y es un artista (consulta API supabase)
    # se verifica que el usuario es propietario de la obra en cuestion (consulta REST API y no lo hace esta funcion, sino el que llama esta funcion)
    # retorna el uuid de usuario
    load_dotenv()
    secret_key = os.getenv('SECRET_KEY')
    algorithm = os.getenv('ALGORITHM')
    pass

def verify_toker_scan(token:  str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
    # se verifica que el usuario existe y es el representante de un scan (consulta API supabase)
    # se verifica que el scan haya tomando el trabajo de traducir la obra (consulta REST API y no lo hace esta funcion, sino el que llama esta funcion)
    # retorna el uuid de usuario
    load_dotenv()
    secret_key = os.getenv('SECRET_KEY')
    algorithm = os.getenv('ALGORITHM')
    pass