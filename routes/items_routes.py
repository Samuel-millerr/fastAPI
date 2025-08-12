from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
items_router = APIRouter(prefix="/items", tags=["itens"])

class Item(BaseModel):
    title: str = None
    is_done: bool = False

items = []

@items_router.post("/")
async def create_item(item: Item):
    items.append(item)
    return f"o item '{item.title}' foi adicionado com sucesso"

@items_router.get("/", response_model=list[Item])
async def list_items(limit: int = 10):
    return items[0:limit]

# FUNÇÕES DE PROCURAR O ITEM POR ID
@items_router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")