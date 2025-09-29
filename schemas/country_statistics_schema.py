from pydantic import BaseModel as SCBaseModel
from typing import Optional

class CountryStatisticsSchema(SCBaseModel):
    id_country_statistics: Optional[int] = None
    id_country: Optional[int] = None
    area: Optional[float] = None
    population: Optional[int] = None
    gdp_usd: Optional[float] = None
    gdp_per_capita: Optional[float] = None
    hdi: Optional[float] = None
    life_expectancy: Optional[int] = None

    class Config:
        from_atributes = True