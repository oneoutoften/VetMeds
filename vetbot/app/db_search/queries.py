from sqlalchemy import select
from app.database.models import Drug
from app.database.connection import Database
from sqlalchemy import bindparam


class DrugSearch:
    def __init__(self, db: Database):
        self.db = db

    async def search_by_name(self, name: str, limit: int = 1) -> list[Drug]:
        async with self.db.get_session() as session:
            query = (
                select(Drug)
                .where(Drug.name.ilike(bindparam("name", f"%{name}%")))
                .limit(limit)
            )
            result = await session.execute(query)
            return result.scalars().all()

    async def search_by_analogs(self, analog: str, limit: int = 1) -> list[Drug]:
        async with self.db.get_session() as session:
            query = (
                select(Drug)
                .where(Drug.name.ilike(bindparam("name", f"%{analog}%")))
                .limit(limit)
            )

            result = await session.execute(query)
            return result.scalars().all()

    async def search_by_active_ingredients(self, active_ingredient: str, limit: int = 1) -> list[Drug]:
        async with self.db.get_session() as session:
            query = (
                select(Drug)
                .where(Drug.name.ilike(bindparam("name", f"%{active_ingredient}%")))
                .limit(limit)
            )

            result = await session.execute(query)
            return result.scalars().all()