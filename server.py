from fastapi import FastAPI
from src.routes import profiles, scans, obras
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

#Middleware 
app.add_middleware(GZipMiddleware, minimum_size=1000)
#Configuracion de las rutas
app.include_router(profiles.profileRoute)
app.include_router(obras.obraRoute)
app.include_router(scans.scanRoute)