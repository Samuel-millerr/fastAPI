from fastapi import APIRouter
from api.v1.routes import country_routes
from api.v1.routes import country_statistics_routes
from api.v1.routes import files

api_router = APIRouter()

api_router.include_router(country_routes.router, prefix="/countries", tags=["Países"])
api_router.include_router(country_statistics_routes.router, prefix="/statistics", tags=["Estatísticas"])
api_router.include_router(files.router, prefix="/file", tags=["Files"])