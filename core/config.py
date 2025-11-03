""" Arquivo para cofigurações gerais da api, como a definição das versões, caminho do banco de dados, declaração do modelos de banco, e assim por diante """
from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1: str = "/api/v1" # Declaração do caminho da API
    
    DB_URL: str = "postgresql+asyncpg://postgres:root@127.0.0.1:5432/escola" # URL do banco de dados

    DBBaseModel = declarative_base()

class Config: 
    case_sensitive = False  
    env_file = ".venv"

settings = Settings() # Classe de configurações passadas para uma variável, utilizada para passar em outros arquivos do projeto
