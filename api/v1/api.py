from fastapi import APIRouter
from api.v1.routes import country_routes

api_router = APIRouter()

api_router.include_router(country_routes.router, prefix="/countries", tags=["Países"])