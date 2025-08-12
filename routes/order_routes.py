from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "você acessou a rota de pedidos"}