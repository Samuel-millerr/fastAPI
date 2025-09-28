from pydantic import BaseModel as SCBaseModel
from typing import Optional, Dict
import json

class CountrySchema(SCBaseModel):
    id_country: Optional[int] = None
    common_name: Optional[str] = None
    official_name: Optional[str] = None
    capital: Optional[str] = None
    continent: Optional[str] = None
    area: Optional[float] = None
    primary_language: Optional[str] = None
    coin_code: Optional[str] = None
    demonym: Optional[str] = None
    flag: Optional[str] = None

    class Config:
        from_atributes = True