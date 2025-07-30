from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import config
from typing import AsyncGenerator
import logging

logger = logging.getLogger(__name__)

Base = declarative_base()

class Database:
    def __init__(self):
        self.engine = None
        self.async_session = None

    async def connect(self):
        try:
            self.engine = create_async_engine(
                config.DB_URL,
                pool_size=20,
                max_overflow=10,
                pool_pre_ping=True,
                echo=False
            )
            self.async_session = sessionmaker(
                bind=self.engine,
                class_=AsyncSession,
                expire_on_commit=False
            )
            logger.info('Database connection established')
        except Exception as e:
            logger.critical(f"Database connection failed: {str(e)}")
            raise

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        if not self.async_session:
            await self.connect()
        async with self.async_session() as session:
            try:
                yield session
                await session.commit()
            except Exception as e:
                await session.rollback()
                logger.error(f"Database error: {str(e)}")
                raise
            finally:
                await session.close()

    async def create_tables(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        logger.info('Database tables created')

database = Database()