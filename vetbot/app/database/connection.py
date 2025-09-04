from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import config
from contextlib import asynccontextmanager


Base = declarative_base()

class Database:
    def __init__(self):
        self.engine = None
        self.async_session = None

    async def connect(self):
        try:
            self.engine = create_async_engine(
                config.DB_URL,
                pool_size=10,
                max_overflow=10,
                pool_pre_ping=True,
                echo=False
            )
            self.async_session = sessionmaker(
                bind=self.engine,
                class_=AsyncSession,
                expire_on_commit=False,
                future=True
            )
        except Exception as e:
            raise

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        if not self.async_session:
            await self.connect()

        async with self.async_session() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


database = Database()