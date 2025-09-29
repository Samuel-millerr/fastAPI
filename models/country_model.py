from core.config import settings
from sqlalchemy import Column, Integer, String

class CountryModel(settings.DBBaseModel):
    __tablename__ = 'paises'

    id_country: int = Column('id_country', Integer(), primary_key=True, autoincrement=True, nullable=False)
    common_name: str = Column('common_name', String(100), nullable=False)
    official_name: str = Column('official_name', String(100), nullable=False)
    capital: str = Column('capital', String(100), nullable=False)
    continent: str = Column('continet', String(100), nullable=False)
    primary_language: str = Column('primary_language', String(20), nullable=False)
    coin_code: str = Column('coin_code', String(3), nullable=True)
    demonym: str = Column('demonym', String(100), nullable=False)
    flag: str = Column('flag', String(255), nullable=True)

