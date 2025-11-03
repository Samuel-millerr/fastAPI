""" Lógica para criação do banco de dados atráves dos models """

from core.config import settings
from core.database import engine
from models import all_models

async def create_tables() -> None:
    print("Criando as tabelas do banco de dados.")

    async with engine.begin() as connection: # Realizando uma conexão assincrona com o banco de dados
        await connection.run_sync(settings.DBBaseModel.metadata.drop_all)
        await connection.run_sync(settings.DBBaseModel.metadata.create_all)

    await engine.dispose()
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(create_tables())
    