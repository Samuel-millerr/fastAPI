from core.config import settings
from sqlalchemy import Column, Integer, String, Float, ARRAY

class CountryModel(settings.DBBaseModel):
    __tablename__ = 'paises'

    id_country: int = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    common_name: str = Column(String(100), nullable=False)
    official_name: str = Column(String(100), nullable=False)
    capital: str = Column(String(100), nullable=False)
    continent: str = Column(String(100), nullable=False)
    area: float = Column(Float(10, 2), nullable=True)
    primary_language: str = Column(String(20), nullable=False)
    coin_code: str = Column(String(3), nullable=True)
    demonym: str = Column(String(100), nullable=False)
    flag: str = Column(String(255), nullable=True)

