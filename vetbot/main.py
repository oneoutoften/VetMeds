import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from app.services import handlers
from app.database.connection import database
from config import config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


async def main():
    try:
        logger.info('Connecting to DB...')
        await database.connect()
        logger.info('DB connected.')

        logger.info('Initializing bot...')
        bot = Bot(
            token=config.TOKEN,
            default=DefaultBotProperties(
                parse_mode='HTML'
            )
        )
        logger.info('Bot initialization completed.')

        dp = Dispatcher()
        dp.include_router(router)

    except Exception as e:
        logger.error(F'Error starting bot: {e}')
        raise

    finally:
        await database.engine.dispose()
        logger.info('DB connection closed.')
        logger.info('Bot\'s been stopped.')