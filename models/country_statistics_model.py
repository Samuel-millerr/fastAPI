from core.config import settings
from sqlalchemy import Column, Float, BigInteger, Integer, ForeignKey


class CountryStatisticsModel(settings.DBBaseModel):
    __tablename__ = 'paises_estatisticas'

    id_country_statistics: int = Column('id_country_statistics', Integer(), primary_key=True, autoincrement=True, nullable=False)
    id_country: int = Column('id_country', ForeignKey("paises.id_country"), nullable=False)
    area: float = Column('area', Float(10, 2), nullable=False)
    population: int = Column('population', BigInteger(), nullable=False)
    gdp_usd: float = Column('gdp_usd', Float(10, 2), nullable=False)
    gdp_per_capita: float = Column('gdp_per_capita', Float(10, 2), nullable=True)
    hdi: float = Column('hdi', Float(10, 2), nullable=True)
    life_expectancy: float = Column('life_expectancy', Float(10, 2), nullable=True)
