from fastapi import FastAPI

app = FastAPI() # Para rodar o código, executar no terminal: uvicorn main:app --reload

from routes.auth_routes import auth_router
from routes.order_routes import order_router
from routes.user_routes import user_router
from routes.items_routes import items_router

app.include_router(auth_router)
app.include_router(order_router)

# app.include_router(user_router)
# app.include_router(items_router)