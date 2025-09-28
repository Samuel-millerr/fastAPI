from pydantic import BaseModel as SCBaseModel
from typing import Optional

class ClassSchema(SCBaseModel):
    id_turma: Optional[int] = None
    nome_turma: str
    padrinho: str
    qtd_alunos: int
    laboratorio: str

    class Config:
        orm_mode = True