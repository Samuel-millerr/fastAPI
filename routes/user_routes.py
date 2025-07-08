from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from random import randint

user_router = APIRouter(prefix="/users", tags=["usuarios"])

users = []

class UserBase(BaseModel):
    nome: str
    email: str

class User(UserBase):
    id: int
    admin: bool = False                 

@user_router.post("/", response_model=User) 
async def register_user(dados: UserBase):
    novo_id = len(users) + 1
    user = User(id=novo_id, **dados.dict())
    users.append(user)    
    raise HTTPException(status_code=201, detail="User Created")

@user_router.get("/")
async def list_users():
    return users
     