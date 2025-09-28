""" O arquivo deps tem como objetivo principal a geração de uma sessão para a conexão entre a API e o nosso banco de dados. 
Dentro da get_session é feita uma importação da sessão já criada no database.py e após isso, essa função é passada para os 
nossos metódos, onde serão consumidos através do Depends."""
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def get_session() -> Generator:
    session: AsyncSession = Session()
    try:
        yield session
    finally:
        await session.close()
