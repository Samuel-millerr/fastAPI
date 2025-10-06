from fastapi import APIRouter, HTTPException, Response, status, Depends
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.all_models import CountryModel
from models.country_statistics_model import CountryStatisticsModel
from schemas.country_statistics_schema import CountryStatisticsSchema
from core.deps import get_session

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CountryStatisticsSchema)
async def create_statistics(statistics: CountryStatisticsSchema, db: AsyncSession = Depends(get_session)):
    new_statistic = CountryStatisticsModel(
        id_country = statistics.id_country,
        area = statistics.area,
        population = statistics.population,
        gdp_usd = statistics.gdp_usd,
        gdp_per_capita = statistics.gdp_per_capita,
        hdi = statistics.hdi,
        life_expectancy = statistics.life_expectancy
    )

    async with db as session:
        query = select(CountryModel).filter(CountryModel.id_country == new_statistic.id_country)
        result = await session.execute(query)
        country = result.scalar_one_or_none()
    
    if not country:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Country not found")

    db.add(new_statistic)
    await db.commit()

    return new_statistic

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[CountryStatisticsSchema])
async def get_statistics(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryStatisticsModel)
        result = await session.execute(query)
        statistics: List[CountryStatisticsModel] = result.scalars().all()

        return statistics
    
@router.get('/{id_statistic}', status_code=status.HTTP_200_OK, response_model=CountryStatisticsSchema)
async def get_statistic(id_statistic: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryStatisticsModel).filter(CountryStatisticsModel.id_country_statistics == id_statistic)
        result = await session.execute(query)
        statistic: CountryStatisticsSchema = result.scalar_one_or_none()

        if statistic:
            pass
        else:
            raise HTTPException(detail="country statistic not found", status_code=status.HTTP_404_NOT_FOUND)
        
@router.patch('/{id_statistic}', status_code=status.HTTP_200_OK, response_model=CountryStatisticsSchema)
async def update_statistic_partial(id_statistic: int, statistic: CountryStatisticsSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryStatisticsModel).filter(CountryStatisticsModel.id_country_statistics == id_statistic)
        result = await session.execute(query)
        statistic_old = result.scalar_one_or_none()

        if statistic_old:
            update_data = statistic.dict(exclude_unset=True)

            for key, value in update_data.items():
                setattr(statistic_old, key, value)  
        
            await session.commit()

            return statistic_old
        else:
            raise HTTPException(detail="country statistic not found", status_code=status.HTTP_404_NOT_FOUND)

@router.delete('/{id_statistic}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_statistic(id_statistic: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CountryStatisticsModel).filter(CountryStatisticsModel.id_country_statistics == id_statistic)
        result = await session.execute(query)
        statistic = result.scalar_one_or_none()

        if statistic:
            await session.delete(statistic)
            await session.commit()

            return {"message": "country statistic successfully delete"}
        else:
            return HTTPException(detail="country statistic not found", status_code=status.HTTP_404_NOT_FOUND)