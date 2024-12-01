from app.database.models import async_session
from app.database.models import Cold_season,  TownCategory
from sqlalchemy import select

async def get_townCategoies():
    async with async_session() as session:
        return await session.scalars(select(TownCategory))

async def get_town(Column_Id):
    async with async_session() as session:
        return await session.scalars(select(Cold_season)
                      .where(Cold_season.Column_Town == Column_Id))

async def get_towm_info(Column_Id):
    async with async_session() as session:
        return await session.scalar(select(Cold_season).where(Cold_season.Column_Id == Column_Id))

