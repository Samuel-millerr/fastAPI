from pydantic.v1 import BaseSettings
from sqlalchemy.orm import declarative_base

class Settings(BaseSettings):
    API_V1: str = "/api/v1"
    DATABASE_URL = "postgresql+asyncpg://postgres:root@127.0.0.1:5432/paises"
    DBBaseModel = declarative_base()

class Config:
    case_sensitive = False
    env_file = ".venv"

settings = Settings()
