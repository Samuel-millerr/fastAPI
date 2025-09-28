""" O database.py tem como objetivo a configuração para a futura conexão do banco com a api """
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession  
from core.config import settings

""" É importante citar que as importações de AsyncEngne e AsyncSession não são nada mais do que 'type hints', ou seja,
serve como facilitação para o código identificar aquela variável com certa função específica """
engine: AsyncEngine = create_async_engine(settings.DB_URL) # O engine é como se fosse o local onde é a base para o funcionamento

Session: AsyncSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False, # Impede que a sessão do banco de dados termine após alguma requisição
    class_=AsyncSession, # Passa para o banco que as sessões criadas serão assincronas
    bind=engine # Conecta a sessão do banco de dados com ao 'motor de funcionamento'   
)
