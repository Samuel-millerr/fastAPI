from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
user_router = APIRouter(prefix="/user", tags=["usuarios"])

class User(BaseModel):
    nome: str = None
    senha: int = None
    email: str = None

@user_router.get("/")
async def verificar_usuario(user: User):
    if user != "admin":
        raise HTTPException(status_code=403, detail="User not authenticated" )
    else:
        return "Acesso liberado"