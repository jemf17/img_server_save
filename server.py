from fastapi import FastAPI
from src.routes import profiles

app = FastAPI()

app.include_router(profiles.profileRoute)

