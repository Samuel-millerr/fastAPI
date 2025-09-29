from fastapi import APIRouter, Response, status, Depends, HTTPException
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.country_model import CountryModel
from schemas.country_schema import CountrySchema
from core.deps import get_session

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CountrySchema)
async def create_country(country: CountrySchema, db: AsyncSession = Depends(get_session)):
    new_country = CountryModel(
        common_name = country.common_name,
        official_name = country.official_name,
        capital = country.capital,
        continent = country.continent,
        primary_language = country.primary_language,
        coin_code = country.coin_code,
        demonym = country.demonym,
        flag = country.flag)
    
    db.add(new_country)
    await db.commit()
    
    return new_country

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[CountrySchema])
async def get_countries(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryModel)
        result = await session.execute(query)
        countries: List[CountryModel] = result.scalars().all()

        return countries
    
@router.get("/{id_country}", status_code=status.HTTP_200_OK, response_model=CountrySchema)
async def get_country(id_country: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryModel).filter(CountryModel.id_country == id_country)
        result = await session.execute(query)
        country = result.scalar_one_or_none()

        if country:
            return country
        else:
            raise HTTPException(detail="country not found", status_code=status.HTTP_404_NOT_FOUND)

@router.patch("/{id_country}", status_code=status.HTTP_200_OK, response_model=CountrySchema)
async def update_country_partial(id_country: int, country: CountrySchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryModel).filter(CountryModel.id_country == id_country)
        result = await session.execute(query)
        country_old = result.scalar_one_or_none()

        if country_old:
            update_data = country.dict(exclude_unset=True)

            for key, value in update_data.items():
                setattr(country_old, key, value)
            
            await session.commit()

            return country_old
        else:
            raise HTTPException(detail="country not found", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{id_country}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(id_country: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryModel).filter(CountryModel.id_country == id_country)
        result = await session.execute(query)
        country = result.scalar_one_or_none()

        if country:
            await session.delete(country)
            await session.commit()

            return {"message": "country successfully delete"}
        else:
            return HTTPException(detail="country not found", status_code=status.HTTP_404_NOT_FOUND)