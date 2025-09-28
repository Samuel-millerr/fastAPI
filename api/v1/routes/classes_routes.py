from fastapi import APIRouter, status, Depends, HTTPException, Response
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.classes_model import ClassModel
from schemas.classes_schema import ClassSchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ClassSchema)
async def create_class(turma: ClassSchema, db: AsyncSession = Depends(get_session)):
    new_class = ClassModel( # Funciona como uma espécie de tradudução entre o json passado pelo usuário
        nome_turma = turma.nome_turma,
        padrinho = turma.padrinho,
        qtd_alunos = turma.qtd_alunos,
        laboratorio = turma.laboratorio)
    
    db.add(new_class) # Adiciona a turma nova ao banco de dados

    await db.commit() # Adicionado quando o autocommit é desativado
    return new_class # Retorna o json da nova turma criada

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[ClassSchema])
async def get_classes(db: AsyncSession = Depends(get_session)):
    """ Lógica utilizada para abrir o banco de dados e realizar uma consulta ou alguma alteração específica, se repete em todos os outros metódos HTTP. """
    async with db as session:
        """ Aqui dentro é aberto uma query de pesquisa """
        query = select(ClassModel)
        result = await session.execute(query)
        classes: List[ClassModel] = result.scalars().all()

        return classes

@router.get("/{id_turma}", status_code=status.HTTP_200_OK, response_model=ClassSchema)
async def get_class(id_turma: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ClassModel).filter(ClassModel.id_turma == id_turma)
        result = await session.execute(query)
        classes = result.scalar_one_or_none() # Retorna uma turma ou nada

        if classes:
            return classes
        else:
            raise HTTPException(detail="Class not found", status_code=status.HTTP_404_NOT_FOUND)

@router.put("/{id_turma}", status_code=status.HTTP_202_ACCEPTED, response_model=ClassSchema)
async def update_class(id_turma: int, turma: ClassSchema,db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ClassModel).filter(ClassModel.id_turma == id_turma)
        result = await session.execute(query)
        classes = result.scalar_one_or_none()

        if classes:
            """ Uma condição que verifica se a turma existe no banco de dados, e caso exista substitui os dados do banco pelo dado passado no json. """
            classes.nome_turma = turma.nome_turma
            classes.padrinho = turma.padrinho
            classes.qtd_alunos = turma.qtd_alunos
            classes.laboratorio =  turma.laboratorio

            await session.commit()

            return classes
        else:
            raise HTTPException(detail="Class not found", status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{id_turma}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_class(id_turma: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ClassModel).filter(ClassModel.id_turma == id_turma)
        result = await session.execute(query)
        classes = result.scalar_one_or_none()

        if classes:
            await session.delete(classes)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="Class not found", status_code=status.HTTP_404_NOT_FOUND)
