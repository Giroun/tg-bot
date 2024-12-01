from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url = 'sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class TownCategory(Base):
    __tablename__ = 'cattegories'
    Column_Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Column_Town: Mapped[str] = mapped_column(String(50))

class Cold_season(Base):
    __tablename__ = 'coldSessionTable'

    Column_Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Column_Town: Mapped[str] = mapped_column(ForeignKey('cattegories.Column_Id'))
    Column_3: Mapped[str]  = mapped_column(String(35))
    Column_4: Mapped[str]  = mapped_column(String(35))
    Column_5: Mapped[str]  = mapped_column(String(35))
    Column_6: Mapped[str]  = mapped_column(String(35))
    Column_7: Mapped[str]  = mapped_column(String(35))
    Column_8: Mapped[str]  = mapped_column(String(35))
    Column_9: Mapped[str]  = mapped_column(String(35))
    Column_10: Mapped[str]  = mapped_column(String(35))
    Column_11: Mapped[str]  = mapped_column(String(35))
    Column_12: Mapped[str]  = mapped_column(String(35))
    Column_13: Mapped[str]  = mapped_column(String(35))
    Column_14: Mapped[str]  = mapped_column(String(35))
    Column_15: Mapped[str]  = mapped_column(String(35))
    Column_16: Mapped[str]  = mapped_column(String(35))
    Column_17: Mapped[str]  = mapped_column(String(35))
    Column_18: Mapped[str]  = mapped_column(String(35))
    Column_19: Mapped[str]  = mapped_column(String(35))
    Column_20: Mapped[str]  = mapped_column(String(35))
    Column_21: Mapped[str]  = mapped_column(String(35))
    Column_22: Mapped[str]  = mapped_column(String(35))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
