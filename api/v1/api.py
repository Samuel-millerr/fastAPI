""" Aqui é onde é definido e organizado os endpoints da api, é feito um uma inserção dos 'routers' dos endpoints dentro dentro de um 'router' geral, que será posteriormente
passado para a api em si """
from fastapi import APIRouter
from api.v1.routes import classes_routes

api_router  = APIRouter()

api_router.include_router(classes_routes.router, prefix="/classes", tags=["Turmas"])