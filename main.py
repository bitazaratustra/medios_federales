from fastapi import FastAPI
from vidoomy.routers.vidoomy import router as vidoomy_router

app = FastAPI()

app.include_router(vidoomy_router)
