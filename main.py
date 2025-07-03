from fastapi import FastAPI

app = FastAPI() # Para rodar o código, executar no terminal: uvicorn main:app --reload

from routes.auth_routes import auth_router
from routes.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)