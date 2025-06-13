from fastapi import APIRouter
from app.routes import muestras, usuarios, auth

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
api_router.include_router(muestras.router, prefix="/muestras", tags=["muestras"])