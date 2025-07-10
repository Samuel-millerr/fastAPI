from fastapi import APIRouter 

person_router = APIRouter(prefix="/person", tags=["pessoa"])

persons = {}

@person_router.post("/")
async def create_person(name: str, idade: int):
    if name == "lari":
        output = "nome de uma pessoa muito bonita, não pode ser adicionado"
    else:
        persons.update({name: idade})
        output = "Pessoa adicionada com sucesso"
    return output

@person_router.get("/")
async def get_persons():
    return persons